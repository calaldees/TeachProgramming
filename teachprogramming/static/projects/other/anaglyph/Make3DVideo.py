#!/usr/bin/env python
import os, sys
from Make3D import process3D_image 

#print (os.listdir('.'))
#print (os.path.exists("iron.png"))
#print '%(language)s has %(#)03d quote types.' % {'language': "Python", "#": 2}
#Python has 002 quote types.

def process3D_video(video_images_left = "L",
                    video_images_right= "R",
                    video_images_out  = "O",
                    image_format      = ".png"   ,
                    image_count_offset_left  =  0,
                    image_count_offset_right =  2,
                    shift_focus              = 10,
                    shift_vertical_left      =  0,
                    shift_vertical_right     = 12,
                    greyscale                = False):
  image_count = 21
  
  def filename_left():
    return "%s%04d%s" % (video_images_left , (image_count + image_count_offset_left ) , image_format)
  def filename_right():
    return "%s%04d%s" % (video_images_right, (image_count + image_count_offset_right) , image_format)
  def filename_out():
    return "%s%04d%s" % (video_images_out  , (image_count                           ) , image_format)
  
  while(os.path.exists(filename_left()) and os.path.exists(filename_right())):
    print "Muxing: %s + %s = %s" % (filename_left(), filename_right(), filename_out())
    process3D_image(filename_left()     ,
                    filename_right()    ,
                    filename_out()      ,
                    shift_focus         ,
                    shift_vertical_left ,
                    shift_vertical_right,
                    greyscale            )
    image_count += 1

process3D_video()