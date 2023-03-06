import os
import json
from typing import TypedDict, Tuple

configFilePath: str = "config.json"

class Config(TypedDict):
	# configure the overlay size/position/dataRate/refreshRate
	size: int
	positionX: int
	positionY: int
	updateDelay: int
	refreshDelay: int

	# where to take the screenshot
	boundingBoxTop: int
	boundingBoxLeft: int
	boundingBoxWidth: int
	boundingBoxHeight: int

	# where to read pixels in the screenshot
	rowTestsX: int
	rowTestsY: Tuple[int,int,int,int]
	spellTestsX: Tuple[int,int,int,int]
	spellTestsY: int
	gridIcon: Tuple[int,int]

	# your spells
	spellGrid: Tuple[
		Tuple[str,str,str,str],
		Tuple[str,str,str,str],
		Tuple[str,str,str,str],
		Tuple[str,str,str,str],
	]

if os.path.isfile(configFilePath):
	with open(configFilePath, "r") as f:
		# TODO clean error if invalid json
		config: Config = json.load(f)
