# https://github.com/KilledByAPixel/LittleJS

serve: game.js engine.all.min.js tiles.png
	python3 -m http.server
game.js:
	curl https://raw.githubusercontent.com/KilledByAPixel/LittleJS/main/game.js -O
engine.all.min.js:
	curl https://raw.githubusercontent.com/KilledByAPixel/LittleJS/main/engine/engine.all.min.js -O
tiles.png:
	curl https://raw.githubusercontent.com/KilledByAPixel/LittleJS/main/tiles.png -O
clean:
	rm -rf *.js
