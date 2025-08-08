Font Masking
============


Looking at
https://nfggames.com/games/fontmaker/lister.php

Many of the fonts are actually 3 values
* transparent
* body (color 1)
* outline/shadow (color 2)
I think many of the fonts can be recreated with primary and secondary surface

TODO: upgrade the font hex loader to 2bit (4 color) per pixel?
Maybe just two hex grids for the same character == 2 masks
Or The gif can have 2 colors? and an editor can be used?
Maybe make a font editor!?


Load a font with a background color/gradient. Masking
* 3 colors?
    * Transparent
    * Primary
    * Secondary
* Primary and Secondary render to a separate image and are used as masks to that image.
    * e.g. they can be flat colous, or they can be gradients/buffer or cycle or animate.
* Gradients are possible with code.
    * Perhaps the gradient can be given multiple colors as paramiters?
    * Draw the font each time 'as needed' and allow drawing to the passthough surface
* See the arcade game typography book for inspiration

Thinking more...
1 bit mask font + with one surface (background)
A font can be composed of two of these (outline and fill) and be composed of two mask surfaces
They can be rendered in order (fill > outline)


Ideas
* Outline
    * Radar
    * Vertical swipe
    * single color bump/fade (animation)
* Fill
    * diagonal gradient
        * Cycle animation

See
https://www.pygame.org/docs/ref/mask.html#pygame.mask.Mask.to_surface
https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/globalCompositeOperation