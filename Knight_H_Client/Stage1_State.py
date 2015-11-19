import random
import json
import os

from pico2d import *
from Player import Player
from Yeti import Yeti
from UI import UI
from Lizard import Lizard
import Game_FrameWork
import Title_State



name = "Stage1"

stage1 = None
player = None
font = None
yeti = None
ui = None
lizard = None


class Stage1:

    def __init__(self):
        self.image = load_image('Stage1(1125x600).png')
        self.backgroundX = 0

    def draw(self):
        self.image.clip_draw(self.backgroundX, 0, 800, 780, 400, 300)
    def setBackgroundX(self, x):
        self.backgroundX = x


        
def enter():
    global stage1, player, yeti, ui, lizard
    stage1 = Stage1()
    player = Player(340)
    yeti = Yeti()
    lizard = Lizard(player.x)
    ui = UI()

def exit():
    global stage1, yeti, player, lizard
    del(yeti)
    del(stage1)
    del(player)
    del(lizard)



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
    global player, yeti, lizard, stage1
    player.update()
    player.setBackgroundX(stage1.backgroundX)
    yeti.update()
    yeti.setBackgroundX(stage1.backgroundX)
    yeti.setPlayerPos(player.x + stage1.backgroundX, player.y)
    lizard.setBackgroundX(stage1.backgroundX)
    lizard.setPlayerState( player.state )
    lizard.setMonsterX( yeti.x )
    lizard.update()
    scroll()



def draw():
    global stage1, player, yeti, lizard

    clear_canvas()
    stage1.draw()
    ui.draw()
    ui.setPlayerHp(player.hp, player.maxHp)
    player.draw()
    lizard.draw()
    yeti.draw()
    update_canvas()

# ----------------
def scroll():
# ----------------
    global stage1, player

    if player.state == player.WALK:
        if player.x >= 640:
            if stage1.backgroundX < 340:
                stage1.backgroundX += 5
        elif player.x <= 150:
            if stage1.backgroundX >= 20:
                stage1.backgroundX -= 5

# ----------------
def collide():
# ----------------
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = a.get_bb()

    if left_a > right_b: return False
    if right_a > left_b: return False
    if top_a > bottom_b: return False
    if bottom_a > top_b: return False




