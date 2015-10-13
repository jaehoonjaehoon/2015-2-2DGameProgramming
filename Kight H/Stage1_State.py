import random
import json
import os

from pico2d import *

import Game_FrameWork
import Title_State



name = "Stage1"

Stage1 = None
font = None



class Stage1:
    def __init__(self):
        self.image = load_image('Stage1(1125x600).png')

    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, 400, 300)


#class Boy:
  #  def __init__(self):
  #      self.x, self.y = 0, 90
 #       self.frame = 0
 #       self.image = load_image('run_animation.png')
 #       self.dir = 1
#
#    def update(self):
      #  self.frame = (self.frame + 1) % 8
     #   self.x += self.dir
    #    if self.x >= 800:
   #         self.dir = -1
  #      elif self.x <= 0:
 #           self.dir = 1
#
 #   def draw(self):
#        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global Stage1
    Stage1 = Stage1()


def exit():
    global Stage1
    del(Stage1)



def pause():
    pass


def resume():
    pass


def handle_events():
     events == get_events()
     for event in events:
         if event.type == SDL_QUIT:
             Game_FrameWork.quit()
         else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_FrameWork.change_state(Title_State)

def update():
    pass

def draw():
    global Stage1

    clear_canvas()
    Stage1.draw()
    update_canvas()




