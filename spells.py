from enum import Enum
from PIL import Image as PilImage
from PIL.Image import Image
from config import config

class Spell:
	def __init__(self, icon: Image, color: "tuple[int, int, int]", cooldown: int) -> None:
		self.icon: Image = icon
		self.color: tuple[int, int, int] = color
		self.cooldown: int = cooldown

RED: 'tuple[int, int, int]' = (130, 27, 0)
GREEN: 'tuple[int, int, int]' = (0, 116, 89)
YELLOW: 'tuple[int, int, int]' = (148, 122, 0)
PURPLE: 'tuple[int, int, int]' = (121, 94, 164)
BLUE: 'tuple[int, int, int]' = (137, 171, 189)

class spells(Spell, Enum):
	accio = PilImage.open('displayicons/accio.png').resize((config['size'],config['size'])), PURPLE, 8
	arresto = PilImage.open('displayicons/arresto.png').resize((config['size'],config['size'])), YELLOW, 15
	avadakedavra = PilImage.open('displayicons/avadakedavra.png').resize((config['size'],config['size'])), GREEN, 90
	bombarda = PilImage.open('displayicons/bombarda.png').resize((config['size'],config['size'])), RED, 15
	confringo = PilImage.open('displayicons/confringo.png').resize((config['size'],config['size'])), RED, 10
	crucio = PilImage.open('displayicons/crucio.png').resize((config['size'],config['size'])), GREEN, 20
	depulso = PilImage.open('displayicons/depulso.png').resize((config['size'],config['size'])), PURPLE, 10
	descendo = PilImage.open('displayicons/descendo.png').resize((config['size'],config['size'])), PURPLE, 10
	desillusionment = PilImage.open('displayicons/desillusionment.png').resize((config['size'],config['size'])), BLUE, 1
	diffindo = PilImage.open('displayicons/diffindo.png').resize((config['size'],config['size'])), RED, 15
	expelliarmus = PilImage.open('displayicons/expelliarmus.png').resize((config['size'],config['size'])), RED, 10
	flipendo = PilImage.open('displayicons/flipendo.png').resize((config['size'],config['size'])), PURPLE, 5
	glacius = PilImage.open('displayicons/glacius.png').resize((config['size'],config['size'])), YELLOW, 10
	imperio = PilImage.open('displayicons/imperio.png').resize((config['size'],config['size'])), GREEN, 30
	incendio = PilImage.open('displayicons/incendio.png').resize((config['size'],config['size'])), RED, 8
	levioso = PilImage.open('displayicons/levioso.png').resize((config['size'],config['size'])), YELLOW, 8
	lumos = PilImage.open('displayicons/lumos.png').resize((config['size'],config['size'])), BLUE, 1
	reparo = PilImage.open('displayicons/reparo.png').resize((config['size'],config['size'])), BLUE, 1
	transformation = PilImage.open('displayicons/transformation.png').resize((config['size'],config['size'])), YELLOW, 20
	wingardiumleviosa = PilImage.open('displayicons/wingardiumleviosa.png').resize((config['size'],config['size'])), BLUE, 1

spellgrid: "list[list[Spell]]" = [
	[spells[config['spellGrid'][y][x]] for x in range(4)]
	for y in range(4)
]
