Copter
======

Code visible at
https://computingteachers.uk/static/projects.html?project=game%2Fcopter

`python3_server.py`
There was no access to `python` on commandline. So I copy and paste into python3 terminal
```python
import http.server, pathlib, functools
http.server.test(
	functools.partial(
		http.server.SimpleHTTPRequestHandler, 
		directory=str(
			pathlib.Path().home().joinpath(
				"OneDrive - Canterbury Christ Church University", 
				"Desktop",
			)
		)
	)
)
```

`python2_server.py`
Place the file with the other assets on desktop. Double click this file to start server.
```python
import SimpleHTTPServer
# SimpleHTTPServer.test()

import SocketServer
PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("0.0.0.0", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
```


`fish.html`
download 
* [fish.gif](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/projects/game/images/fish.gif)
* [FishLevel1.gif](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/projects/game/images/FishLevel1.gif)
```javascript
<canvas id="canvas_element" width="320" height="240" style="image-rendering: pixelated; object-fit: contain; width:100%; max-width: 100%; height: 100%; max-height: 100%;">
</canvas>
<canvas id="canvas_colisions" width="320" height="240" style="display: none"></canvas><!-- // -->
<script>
    const canvas = document.getElementById('canvas_element');
    const context = canvas.getContext('2d');

    let paused;
    function start() {paused = false; requestAnimationFrame(timerEvent);}
    function pause() {paused = true;}

    const keys = {
        27: 'ESCAPE',
        32: 'SPACE'
    };
    const keys_pressed = {};
    function init_keys() {for (let key in keys) {keys_pressed[keys[key]]=false;}}
    window.addEventListener('keydown', eventKeyDown, true);
    window.addEventListener('keyup'  , eventKeyUp  , true);
    function eventKeyDown(event) {
        if (event.keyCode in keys) {
            keys_pressed[keys[event.keyCode]]=true;  event.preventDefault();
        }
    }
    function eventKeyUp(event) {
        if (event.keyCode in keys) {
            keys_pressed[keys[event.keyCode]]=false; event.preventDefault();
        }
    }

    const colisions_context = document.getElementById('canvas_colisions').getContext('2d');

    const v = {
        "color_background": `rgba(0,0,0,255)`,
        "color_background": `rgba(0,0,255,255)`,
    };

    v.copter_image = new Image();
    v.copter_image.src = `images/fish.gif`;
    v.background_image = new Image();
    v.background_image.src = `images/FishLevel1.gif`;


    function reset() {
        init_keys();
        v.view_x_pos   =  0;
        v.copter_x_pos = 50;
        v.copter_y_pos = canvas.height / 2;
    }

    function timerEvent() {
        context.fillStyle = v.color_background;
        context.fillRect(0, 0, canvas.width, canvas.height);

        v.view_x_pos += 1
        context.drawImage(v.background_image, -v.view_x_pos, 0);

        if (keys_pressed.ESCAPE) {pause(); reset();}
        if (keys_pressed.SPACE) {v.copter_y_pos+=-2;}
        else                    {v.copter_y_pos+= 1;}

        colisions_context.fillStyle = v.color_background;
        colisions_context.fillRect(0, 0, canvas.width, canvas.height);
        colisions_context.drawImage(v.background_image, -v.view_x_pos, 0);

        const point = [v.copter_image.width/2, v.copter_image.height/2];
            const [r,g,b,a] = colisions_context.getImageData(
                v.copter_x_pos+point[0],
                v.copter_y_pos+point[1], 1, 1).data;
            const pixel_color = `rgba(${r},${g},${b},${a})`;
            if (pixel_color != v.color_background) {
                reset();
            }

        context.drawImage(
            v.copter_image, Math.round(v.copter_x_pos), Math.round(v.copter_y_pos),
        );

        if (!paused) {requestAnimationFrame(timerEvent);}
    }

    reset();
    start();
</script>
```

Reference
---------

* The fight to get python server working on CCCU curriculum machines
    * 4+ different versions of python installed (this needs to be audited!!!)
    * [http.server (command) fails to bind dual-stack on Windows](https://bugs.python.org/issue39211)
    * SimpleHTTPServer python2
        * https://docs.python.org/2/library/simplehttpserver.html
        * https://github.com/python/cpython/blob/v2.7/Lib/SimpleHTTPServer.py
    * http.server
        * https://docs.python.org/3/library/http.server.html
        * https://github.com/python/cpython/blob/main/Lib/http/server.py


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



Copter Simple 3
===============

```python {.line-numbers}
import pygame
from animation_base_pygame import PygameBase

class CopterGame(PygameBase):
    def __init__(self):
        self.background_color = (0, 0, 255, 255)
        self.background_image = pygame.image.load("images/FishLevel1.gif")
        self.copter_image     = pygame.image.load("images/fish.gif")
        self.reset()
        super().__init__()
    def reset(self):
        self.background_x_pos = 0
        self.copter_x_pos = 50
        self.copter_y_pos = 100
    def loop(self, screen, frame):

        self.background_x_pos += 1
        if self.keys[pygame.K_SPACE]: 
            self.copter_y_pos += -2
        else: 
            self.copter_y_pos +=  1

        collision_point = (self.copter_x_pos + self.background_x_pos, self.copter_y_pos)
        try   : pixel = self.background_image.get_at(collision_point)
        except: pixel = None
        if pixel and pixel != (255,255,255,255):
            self.reset()

        pygame.draw.rect(screen, self.background_color, (0,0)+screen.get_size())
        screen.blit(self.background_image, (-self.background_x_pos, 0))
        screen.blit(self.copter_image, (self.copter_x_pos, self.copter_y_pos))

if __name__ == '__main__':
    CopterGame().run()
```


---

Copter
======

```diff

```