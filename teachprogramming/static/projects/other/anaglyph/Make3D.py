#!/usr/bin/env python
import sys, getopt
from PIL import Image, ImageOps

# -- References --
# Gimp Tutorial
#  http://graphicssoft.about.com/od/gimp/ht/3danaglyph.-UkA.htm
# Layer Merging Maths
#  http://www.mirrorservice.org/sites/docs.gimp.org/en/gimp-concepts-layer-modes.html
# Python Image Library
#  http://www.pythonware.com/library/pil/handbook/image.htm


#--------Helpers------------
def enforce255(a):
  if a < 0   : return 0
  if a > 255 : return 255
  return int(a)
def layer_screen(a,b):
  return enforce255(255 - ( ((255-a)*(255-b)) /255))
def layer_multiply(a,b):
  return enforce255( (1/float(255))*(a*b) )

#--------Process 3D Image----------
def process3D_image(filename_left        = "l.png",
                    filename_right       = "r.png",
                    filename_out         = "o.png",
                    shift_focus          = 0,
                    shift_vertical_left  = 0,
                    shift_vertical_right = 0,
                    greyscale            = False):
  
  #--------Load Images-----------
  image_left  = Image.open(filename_left)
  image_right = Image.open(filename_right)
  image_out   = Image.new(image_left.mode, (image_left.size[0]-shift_focus,image_left.size[1]-max(shift_vertical_left, shift_vertical_right)))
  
  if (greyscale==True):
    image_left  = ImageOps.grayscale(image_left ).convert("RGB")
    image_right = ImageOps.grayscale(image_right).convert("RGB")
  
  l = image_right.load() #HACK WARNING! HACK WARNING! Because im a twonk the L and R images are processed the wrong way round in the code below, so I hacked them to swap here
  r = image_left.load()
  o = image_out.load()
  
  #--------Process Pixels----------
  for x in range(image_out.size[0]):
    for y in range(image_out.size[1]):
      #Screen the left pixel against red
      pixel_left = l[x+shift_focus,y+shift_vertical_left]
      processed_pixel_left = (layer_screen(pixel_left[0],255),
                              layer_screen(pixel_left[1],  0),
                              layer_screen(pixel_left[2],  0) )
      #Screen the right pixel against cyan
      pixel_right = r[x,y+shift_vertical_right]
      processed_pixel_right = (layer_screen(pixel_right[0],  0),
                               layer_screen(pixel_right[1],255),
                               layer_screen(pixel_right[2],255) )
      #Multiply the left and right layers
      processed_pixel_merged = (layer_multiply(processed_pixel_right[0],processed_pixel_left[0]),
                                layer_multiply(processed_pixel_right[1],processed_pixel_left[1]),
                                layer_multiply(processed_pixel_right[2],processed_pixel_left[2]) )
      o[x,y] = processed_pixel_merged
  
  #--------Save---------
  image_out.save(filename_out)
  
  
#--------Command Line Arguments---------
def usage():
  print (sys.argv[0] + " some stuff")
  
def main(argv):
  options = {}
  try:
    opts, args = getopt.getopt(argv, "hl:r:o:f:g", ["help","filename_left=", "filename_right=", "filename_out=", "shift_focus=", "shift_vertical_left=", "shift_vertical_right=", "greyscale"])
  except getopt.GetoptError:
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    elif opt in ("-l", "--filename_left"       ): options['filename_left'       ] = arg
    elif opt in ("-r", "--filename_right"      ): options['filename_right'      ] = arg
    elif opt in ("-o", "--filename_out"        ): options['filename_out'        ] = arg
    elif opt in ("-f", "--shift_focus"         ): options['shift_focus'         ] = int(arg)
    elif opt in (      "--shift_vertical_left" ): options['shift_vertical_left' ] = int(arg)
    elif opt in (      "--shift_vertical_right"): options['shift_vertical_right'] = int(arg)
    elif opt in ("-g", "--greyscale"           ): options['greyscale'           ] = True
  process3D_image(**options)

if __name__ == "__main__":
    main(sys.argv[1:])