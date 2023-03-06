# Respellio
A spell overlay for Hogwarts Legacy. Yes the name is terrible but whatever.

## Why
When playing Hogwarts Legacy, I often wonder what's the current state of cooldowns for spells not in the active spellset, and I can't switch spellsets mid-fight just to check that and find out that spells are not even ready yet.

Also sometimes I'm in a spellset and I don't remember if I have to scroll up or down to get to the spellset I want.

## What
This project adds an overlay that displays the spell table during fights, which allows to see all spellsets and be able to easily switch to any spellset, and also see all cooldowns.
![Example](https://user-images.githubusercontent.com/102462519/223238435-3d16d6c0-230f-40c1-8664-481556f20207.png)

## Limitations
- This overlay reads information on the screen, not really efficient.
- For this reason, the game has to run in borderless window mode.
- Cooldowns are using the base value. If you have the talent that reduces cooldowns for each basic hit, your actual cooldowns might be faster than what the overlay says.
- It is only thought for KB/M users (for now?) with the table/rows layouts, not diamond layouts.

## How to use
* Edit `config.json` so that detection values correspond to your screen (see below)<br>
relevant attributes:
  - boundingBoxTop
  - boundingBoxLeft
  - boundingBoxWidth
  - rowTestsX
  - rowTestsY
  - spellTestsX
  - spellTestsY
  - gridIcon
* Edit `config.json` so that the overlay is displayed somewhere smart (default is top left corner, which is never practical but it's valid on every screen)<br>
relevant attributes:
  - size
  - positionX
  - positionY
* Edit `config.json`to specify your spells
* Have your "displayicons" folder ready next to the .exe
* Run the .exe (maybe nothing will happen except a tray icon will appear)
* Enjoy the game with the overlay
* Exit the overlay by right clicking the tray icon and selecting "Exit"

3440x1440 values:
```json
	"boundingBoxTop": 1058,
	"boundingBoxLeft": 2866,
	"boundingBoxWidth": 556,
	"boundingBoxHeight": 204,

	"rowTestsX": 540,
	"rowTestsY": [94, 121, 147, 174],
	"spellTestsX": [66, 197, 327, 458],
	"spellTestsY": 77,
	"gridIcon": [491, 15],
```

2560x1440 values:
```json
	"boundingBoxTop": 1058,
	"boundingBoxLeft": 1986,
	"boundingBoxWidth": 556,
	"boundingBoxHeight": 204,

	"rowTestsX": 540,
	"rowTestsY": [94, 121, 147, 174],
	"spellTestsX": [66, 197, 327, 458],
	"spellTestsY": 77,
	"gridIcon": [491, 15],
```

1920x1080 values:
```json
	"boundingBoxTop": 797,
	"boundingBoxLeft": 1494,
	"boundingBoxWidth": 415,
	"boundingBoxHeight": 153,

	"rowTestsX": 401,
	"rowTestsY": [67, 87, 107, 127],
	"spellTestsX": [45, 143, 241, 339],
	"spellTestsY": 56,
	"gridIcon": [358, 7],
```

## How to find detection values for your own screen
Basically the program takes a screenshot of a small portion of the screen then tries to read pixels on it. The smaller the area, the better the performances. But the area needs to have all information in it.
So the values you provide tell the program where to take the screenshot and where to read pixels on the screenshot.
Here are two screenshots explaining where the values come from for the case of 3440x1440.

![Example](https://user-images.githubusercontent.com/102462519/223568236-d33e0ba5-ceaa-4b94-a99e-b5c112813806.png)
![Example](https://user-images.githubusercontent.com/102462519/223568258-aef87710-add2-40ca-b0c3-45555e8913a7.png)

## Position values

These values position the overlay on screen.
I can only speak for 3440x1440, and my personal values are the following:
```
	"size": 80,
	"positionX": 3000,
	"positionY": 700,
```
This puts the overlay on top of the duelling feats so yeah, you can't read duelling feats anymore... Probably use another value for positionY to move it elsewhere.
