import random
import json
import os

from pico2d import *
from Player import Player

import Game_FrameWork
import Title_State



name = "Stage1"

stage1 = None
player = None
font = None



class Stage1:
    def __init__(self):
        self.image = load_image('Stage1(1125x600).png')

    def draw(self):
        self.image.clip_draw(300, 0, 800, 780, 400, 300)



def enter():
    global stage1
    global player
    stage1 = Stage1()
    player = Player()


def exit():
    global stage1
    global player
    del(stage1)
    del(player)



def pause():
    pass


def resume():
    pass


def handle_events():
    global player

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            Game_FrameWork.quit()
        else:
           if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
               Game_FrameWork.change_state(Title_State)
           else:
              player.handle_events(event)

def update():
    global player
    player.update()

def draw():
    global stage1
    global player

    clear_canvas()
    stage1.draw()
    player.draw()
    update_canvas()




