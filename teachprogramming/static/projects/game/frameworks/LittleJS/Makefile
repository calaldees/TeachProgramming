# https://github.com/KilledByAPixel/LittleJS
# https://killedbyapixel.github.io/LittleJS/examples/box2d/
# https://js13kgames.com/2024/games/data-warrior-13kb-limit

serve: game.js littlejs.min.js tiles.png
	python3 -m http.server
game.js:
	curl https://raw.githubusercontent.com/KilledByAPixel/LittleJS/main/examples/starter/game.js -O
littlejs.min.js:
	curl https://raw.githubusercontent.com/KilledByAPixel/LittleJS/main/build/littlejs.min.js -O
tiles.png:
	curl https://raw.githubusercontent.com/KilledByAPixel/LittleJS/main/examples/starter/tiles.png -O
clean:
	rm -rf *.js
