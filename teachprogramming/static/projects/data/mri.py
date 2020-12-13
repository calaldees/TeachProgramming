# https://nipy.org/nibabel/gettingstarted.html
import os
import numpy as np
import nibabel as nib

def get_mri():
    #from nibabel.testing import data_path
    #example_filename = os.path.join(data_path, 'example4d.nii.gz')
    #example_filename = 'vol0000.nii.gz'
    example_filename = 'T1_T2FLAIR_fMRI.nii.gz'

    img = nib.load(example_filename)
    print(img.shape)
    print(img.header)
    data = img.get_fdata()
    print(data.shape)
    return data


import pygame as pg

class GameBase():
    def __init__(self, title="pg", resolution=(320,180), fps=60, color_background='black'):
        pg.init()
        pg.display.set_caption(title)
        self.screen = pg.display.set_mode(resolution, pg.SCALED | pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.fps = fps
        self.color_background = color_background
    def run(self):
        frame = 0
        self.running = True
        while self.running:
            self.clock.tick(self.fps)
            self.keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                    self.running = False
                if event.type == pg.VIDEORESIZE:
                    pg.display._resize_event(event)
                if (self.keys[pg.K_RALT] or self.keys[pg.K_LALT]) and self.keys[pg.K_RETURN]:
                    pg.display.toggle_fullscreen()
            self.screen.fill(self.color_background)
            self.loop(self.screen, frame)
            pg.display.flip()
            frame += 1
        self.quit()
        pg.quit()
    def loop(self, screen, frame):
        raise NotImplementedError('override loop method')
    def quit(self):
        pass  # override to shutdown

class Game(GameBase):
    def __init__(self):
        #self.x = 100
        #self.y = 100
        self.z = 100
        self.data = get_mri()
        super().__init__()
    def loop(self, screen, frame):
        if self.keys[pg.K_UP]:
            self.z += 1
        if self.keys[pg.K_DOWN]:
            self.z += -1


        #pg.draw.rect(screen, 'green', (self.x, self.y, 70, 40), 2, border_radius=15)
        #screen.blit(self.image, (self.x, self.y))
        for y in range(self.data.shape[1]):
            for x in range(self.data.shape[0]):
                i = int(self.data[x][y][self.z][0])
                pg.draw.rect(screen, (i,i,i), (x, y, 1, 1))
                #pg.gfxdraw.pixel(screen, x, y, (i,i,i))


if __name__ == '__main__':
    Game().run()
