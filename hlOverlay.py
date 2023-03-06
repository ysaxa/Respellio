import math

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PIL import Image as PilImage, ImageDraw, ImageGrab

from config import *
from ui import *


def pixelDistance(p1: 'tuple[int,int,int]', p2: 'tuple[int,int,int]') -> float:
	return math.sqrt(pow(p1[0]-p2[0], 2)+pow(p1[1]-p2[1], 2)+pow(p1[2]-p2[2], 2))

class GridUpdater():
	def __init__(self, form: Overlay) -> None:
		self.form: Overlay = form
		pass

	def updateGrid(self) -> None:
		#TODO read in config
		boundingBox: 'tuple[int,int,int,int]' = (config['boundingBoxLeft'], config['boundingBoxTop'], config['boundingBoxWidth'], config['boundingBoxHeight'])
		boundingBox = (boundingBox[0],boundingBox[1],boundingBox[0]+boundingBox[2],boundingBox[1]+boundingBox[3])
		rowtests: 'list[tuple[int,int]]' = [  # where to test pixel color to find active row
			(config['rowTestsX'], config['rowTestsY'][i]) for i in range(4)
		]
		spelltests: 'list[tuple[int,int]]' = [ # where to test pixel to detect if spell was used
			(config['spellTestsX'][i], config['spellTestsY']) for i in range(4)
		]
		gridicon: tuple[int,int] = (config['gridIcon'][0], config['gridIcon'][1]) # where to test if the ui is displayed

		# take a screenshot of speelsets in game
		spellSetShot: Image = ImageGrab.grab(bbox=boundingBox)

		# activate or deactivate the overlay if spells are not displayed on screen
		pixel: 'tuple[int,int,int]' = spellSetShot.getpixel(gridicon) # type: ignore
		overlayActive: bool = pixel[0]>250 and pixel[1]>250 and pixel[2]>250

		form.isActive = overlayActive

		# find which of the indicators is the whitest among the four row indicators
		rowpixels: 'list[tuple[int,int,int]]' = [spellSetShot.getpixel(pos) for pos in rowtests] # type: ignore
		distances: list[float] = [pixelDistance(p, (255,255,255)) for p in rowpixels]
		activerow:int = [i for i,d in enumerate(distances) if d == min(distances)][0]

		# set active row to the row found above
		self.form.activerow = activerow

		# study all four spells in the current set and update lastUsed if any is grey
		if overlayActive:
			for x in range(4):
				pixel: 'tuple[int,int,int]' = spellSetShot.getpixel(spelltests[x]) # type: ignore
				if pixel[0]==pixel[1] and pixel[1]==pixel[2] and pixel[0]<30:
					relevantSpellIndicator: SpellIndicator = self.form.spellgrid[activerow][x]
					if relevantSpellIndicator.lastUsed < now()-relevantSpellIndicator.spell.cooldown:
						relevantSpellIndicator.lastUsed = now()

if __name__ == '__main__':
	app: QApplication = QApplication([])
	form: Overlay = Overlay(spellgrid)

	def drawIcon() -> Image:
		image: Image = PilImage.new('RGBA', (64, 64), (0, 0, 0, 255))
		draw: ImageDraw.ImageDraw = ImageDraw.Draw(image)

		draw.ellipse([(17, 24), (46, 53)], fill="black", width=2, outline="white")

		draw.line([(31,11), (31,53)], fill="white", width=2)

		draw.line([(31,11), (7,52)], fill="white", width=2)
		draw.line([(7,52), (56,52)], fill="white", width=2)
		draw.line([(56,52), (31,11)], fill="white", width=2)

		return image

	icon: QIcon = QIcon(QPixmap.fromImage(ImageQt(drawIcon())))
	tray: QSystemTrayIcon = QSystemTrayIcon()
	tray.setIcon(icon)
	tray.setVisible(True)

	menu: QMenu = QMenu()
	action: QAction = QAction("Exit")
	action.triggered.connect(lambda: app.quit())
	menu.addAction(action)
	tray.setContextMenu(menu)

	gridUpdater: GridUpdater = GridUpdater(form)
	def updateGrid() -> None:
		gridUpdater.updateGrid()
	timer1: QTimer = QTimer()
	timer1.timeout.connect(updateGrid)
	timer1.start(config['updateDelay']) #TODO read in config

	timer2: QTimer = QTimer()
	timer2.timeout.connect(form.updateGrid)
	timer2.start(config['refreshDelay'])

	app.exec()
