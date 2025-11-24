Computer Graphics Foundations


https://flashtro.com/flashtro-morton-strikes-back/


* [terminal2.cs](../projects/graphics/terminal2.cs)
    * https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
        * Integer only
* [pygame_zoomer.py](../projects/game/pygame_zoomer.py)
    * functional - no state
    * sin animations
* [synth.py](../projects/sound/synth.py)
    * tracker
    * 8bit unsigned audio samples
* [1stPersonRaycast.html](../projects/game/1stPersonRaytrace.html)
    * [Raycast2.html](../projects/game/Raycast2.html)
* font mask
    * https://nfggames.com/games/fontmaker/lister.php
    * old [font_mask.html](https://calaldees.dreamhosters.com/misc/font_mask.html)
    * [font_mask.html](../projects/graphics/font/font_mask.html)

```bash
cd ~/code/personal/TeachProgramming/teachprogramming/static/projects/

python3 -m http.server

csharp graphics/terminal2.cs
uv run --with pygame game/pygame_zoomer.py
uv run --with pygame graphics/font/font_pygame.py
cd sound && uv run --with pyaudio synth.py

open http://localhost:8000/game/1stPersonRaytrace.html
open http://localhost:8000/graphics/font/font.html
```