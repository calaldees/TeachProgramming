Font Project
============

Create a class raster font using image encoding to hex, http post requests (command line?), html viewer (channelServer), output as png, use font in their own programs

* use `Makefile` to run `docker` container on server/ip that young people can access
* visit http://??? and start making a font
  * using `curl`
  * print out `template.odt` with lookup table
* Look at `python`/`pygame` snippets below for loading font

* https://github.com/calaldees/mapOfComputing/blob/main/computing/typography.md
    * [ZX Origins](https://damieng.com/typography/zx-origins) - 8x8 mono bitmap fonts
    * [BitmapFonts](https://github.com/ianhan/BitmapFonts/blob/main/README.md)
        * My collection of bitmap fonts pulled from various demoscene archives over the years
    * [NFG's Arcade Font Engine](https://nfggames.com/games/fontmaker/lister.php)
        * https://nfggames.com/games/fontmaker/ (with gradient!!! Cool!)
        * Apply gradient to white letters
        * 2color (on/off) - 4 color (transparent,gradient-passthrough,solid-color,shadow(50%transparent-gradient?))?
* Demoscene "Greets" - code-alias - creativity

### TODO
* Raster fonts are not vector fonts
* Edit a vector font?

---

Template
========

|<br>| | | | | | | |
|-|-|-|-|-|-|-|-|
|<br>| | | | | | | |
|<br>| | | | | | | |
|<br>| | | | | | | |
|<br>| | | | | | | |
|<br>| | | | | | | |
|<br>| | | | | | | |
|<br>| | | | | | | |

| | |
|-|-|
0000 = 0 = 0 | 1000 = 8 = 8
0001 = 1 = 1 | 1001 = 9 = 9
0010 = 2 = 2 | 1010 = a = 10
0011 = 3 = 3 | 1011 = b = 11
0100 = 4 = 4 | 1100 = c = 12
0101 = 5 = 5 | 1101 = d = 13
0110 = 6 = 6 | 1110 = e = 14
0111 = 7 = 7 | 1111 = f = 15


---

OLD
===
* Concept for encoding a character from a raster font set in hex and sending that to a DB via an http api
* Teacher projects fontset on html5 display
* [fontLiveView.html](./fontLiveView.html)
    * use channelServer
* use channelServer http get - url components
* Database?
    * Connect to channelServer and 'append to file' the items that are sent
* Export to PNG? ASCII order?
    * https://www.ascii-code.com/
    * symbols 32-47 + 58-64 + 91-96 + 123-126
    * 0 == 48
    * A == 65
    * a == 97
    * 0-255 array as empty 8x8 images, then a loader to put chars in correct ascii locations? 3 images(or rows?)0-9,A-Z,a-z
* TODO
    * Make data to gif python exporter
    * Make image cutter to ascii codes



<style>
@media print {
    hr {display: none;}
    h1 {page-break-before: always;}
    h1:first-of-type {page-break-before: avoid;}
}
pre[class*="language-"] {background-color: #e7e7e7; border: 1px grey solid;} /* code blocks print visibly on paper*/
.token.inserted {font-weight: bolder; color: green;}
.token.deleted {text-decoration: line-through; color: red;}
</style>

---
<hr style="page-break-after: always;"/>

Fonts
=====

Draw character
--------------

```python
import pygame
from animation_base_pygame import PygameBase
from pathlib import Path

class PygameFont(PygameBase):
    def __init__(self):
        self.font = self.load_font()
        super().__init__(resolution=(320,180))
    def load_font(self, path_font=Path('font.gif')):
        img = pygame.image.load(path_font)
        return {chr(i): img.subsurface((i*8, 0, 8, 8)) for i in range(img.get_width()//8)}
    def loop(self, screen, frame):
        self.screen.blit(self.font["a"], (100, 100))

if __name__ == '__main__':
    PygameFont().run()
```

Draw string
-----------

```diff
+    def draw_font(self, text, x, y):
+        for i, char in enumerate(text):
+            self.screen.blit(self.font[char], (x+i*8, y))
     def loop(self, screen, frame):
+        w, h = screen.get_size()
+        self.draw_font("abcde", frame%w, 50)
         self.screen.blit(self.font["a"], (100, 100))
```

Automatic font download
-----------------------

```diff
from pathlib import Path
+from urllib.request import urlopen
...
-    def load_font(self, path_font=Path('font.gif')):
+    def load_font(self, path_font=Path('font.gif'), url_font='http://localhost:8000/static/font.gif'):
+        if not path_font.exists():
+            with urlopen(url_font) as r, path_font.open(mode='wb') as f:
+                f.write(r.read())
         img = pygame.image.load(path_font)
```

Draw sin wave
-------------

```diff
 from urllib.request import urlopen
+import math

...
+    def draw_font_wave(self, text, x, y):
+        for i, char in enumerate(text):
+            _x = x+i*8
+            _y = y + math.sin(_x/50)*50
+            self.screen.blit(self.font[char], (_x, _y))
     def loop(self, screen, frame):
...
         self.draw_font("abcde", frame%width, 50)
+        self.draw_font_wave("abcde", frame%w, 110)
```

Super advanced font loader
--------------------------

(This is intended for Advanced GCSE and A-Level students)

```python
# https://damieng.com/typography/zx-origins/
# curl https://images.damieng.com/fonts/zx-origins/Prince.png -o font.png
SEQUENCE_ZX_ORIGINS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_£abcdefghijklmnopqrstuvwxyz{|}~©"""
#...
-    self.font = self.load_font()
+    self.font = self.load_font_advanced()
#...
     super().__init__(resolution=(320,180), color_background='white')
#...
    def load_font_advanced(self, path_font=Path('font.png'), seq=SEQUENCE_ZX_ORIGINS, w=8, h=8):
        img = pygame.image.load(path_font)
        ww, hh = img.get_size()
        return {
            seq[i]: img.subsurface(((i*w)%ww, ((i*w)//ww)*h, w, h))
            for i in range(min((ww//w)*(hh//h), len(seq)))
        }
```

* https://damieng.com/typography/zx-origins
* https://github.com/ianhan/BitmapFonts/
* https://nfggames.com/games/fontmaker/ see: "All fonts on one page"