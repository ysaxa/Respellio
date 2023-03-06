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
- Edit `config.json` so that values correspond to your screen (see below)
- Maybe edit other values to change the size/position/whatever of the overlay
- Have your "displayicons" folder ready next to the .exe
- Run the .exe (maybe nothing will happen except a tray icon will appear)
- Enjoy the game with the overlay
- Exit the overlay by right clicking the tray icon and selecting "Exit"

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

	"rowTestsX": 0, // I DON'T KNOW, SOMEONE PLEASE SEND ME A SCREENSHOT OF THE GAME IN 1080P WITH KB/M
	"rowTestsY": [0, 0, 0, 0],
	"spellTestsX": [49, 148, 246, 345],
	"spellTestsY": 60,
	"gridIcon": [357, 10],
```

