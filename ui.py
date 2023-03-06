from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QGridLayout
from PIL import Image as PilImage, ImageDraw
from PIL.ImageQt import ImageQt

from spells import *
from config import config

import datetime;

def now() -> float:
	return datetime.datetime.now().timestamp()

class SpellIndicator:
	def __init__(self, spell: Spell) -> None:
		self.spell: Spell = spell # the spell that gives the icon or the cooldown time
		self.lastUsed: float = 1
		self.label: QLabel # qt label in the displayed grid layout

class Overlay(QtWidgets.QWidget):
	def __init__(self, spellgrid: "list[list[Spell]]") -> None:
		global alive

		self.isActive: bool = False
		self.oldIsActive: bool = False

		self.activerow: int = 0 # number that represents the currently active row
		self.oldactiverow: int = 0

		super().__init__()
		self.spellgrid: list[list[SpellIndicator]] = [
			[SpellIndicator(spellgrid[y][x]) for x in range(4)]
			for y in range(4)
		]
		self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
		self.setWindowFlags(
			QtCore.Qt.WindowStaysOnTopHint |
			QtCore.Qt.FramelessWindowHint |
			QtCore.Qt.Tool
		)
		self.gridLayout: QGridLayout = QGridLayout(self)

		for x in range(4):
			for y in range(4):
				label: QLabel = QLabel()
				self.gridLayout.addWidget(label, y, x)
				self.spellgrid[y][x].label = label

		# prepare images that are going to be used frequently
		self.rectangle: Image = PilImage.new('RGBA', (config['size'], config['size']), (0, 0, 0, 255))
		draw: ImageDraw.ImageDraw = ImageDraw.Draw(self.rectangle)
		draw.rectangle((0,0, config['size']-1,config['size']-1), fill=(0,0,0,0), outline="white", width=2)

		self.noImage: Image = PilImage.new('RGBA', (config['size'], config['size']), (0, 0, 0, 0))


		self.updateGrid()
		self.move(config['positionX'], config['positionY'])
		self.show()

	def updateGrid(self) -> None:
		if not self.isActive and not self.oldIsActive: return

		for x in range(4):
			for y in range(4):
				spellindic: SpellIndicator = self.spellgrid[y][x]
				label: QLabel = spellindic.label

				#if spellindic.lastUsed == 0 and self.oldactiverow - self.activerow == 0: continue

				# generate image
				height: int = int(config['size']*min(1.0, (now()-spellindic.lastUsed)/spellindic.spell.cooldown))
				if height == config['size']: spellindic.lastUsed = 0 # magic

				image: Image = self.noImage
				if self.isActive: # not sure why pylance is lost since this 'if' was added
					image: Image = PilImage.new('RGBA', (config['size'], config['size']), (0, 0, 0, 255))
					filling: Image = PilImage.new('RGBA', (config['size'], height), tuple(map(lambda x: int(x*0.7), spellindic.spell.color)) if spellindic.lastUsed != 0 else spellindic.spell.color)
					image.paste(filling, (0, config['size']-height), filling) # third argument for transparency
					image.paste(spellindic.spell.icon, (0, 0), spellindic.spell.icon)
					if y==self.activerow: image.paste(self.rectangle, (0, 0), self.rectangle)

				pixmap: QPixmap = QPixmap.fromImage(ImageQt(image)) # type: ignore
				label.setPixmap(pixmap)
				label.resize(pixmap.width(), pixmap.height())

		self.oldIsActive = self.isActive
		self.oldactiverow = self.activerow
