Animation Base
==============

TODO:
* Cut Sub Image
    * Maybe from name? "filename.gif:??"
* Get Pixel (from screen)
* Put Pixel
* Filled Polygon


The concept needs rethinking
We need
Model (separate from drawing. Key state passed as input (allowing for recording. Random from lookup? to allow functional?))
Draw (from model as a separate step - draw to backbuffer/surface/context/image)
Loop, IMMEDIATLY draw backbuffer (this will help smoothness)

Consider keyboard input for turn (minesweeper? prevent runaway repeat? perhaps just set back to false when consumed?)