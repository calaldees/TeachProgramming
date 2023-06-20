Font Project
============

Create a class raster font using image encoding to hex, http post requests (command line?), html viewer (channelServer), output as png, use it


Raster font network?
===================
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
* https://nfggames.com/games/fontmaker/lister.php
    * https://nfggames.com/games/fontmaker/index.php (with gradient!!! Cool!)
    * Apply gradient to white letters
    * 2color (on/off) - 4 color (transparent,gradient-passthrough,solid-color,shadow(50%transparent-gradient?))?
* Demoscene "Greets" - code-alias - creativity

* Raster fonts are not vector fonts
* Edit a vector font?
