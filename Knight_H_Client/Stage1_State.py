import random
import json
import os

from pico2d import *
from Player import Player
from Yeti import Yeti
from UI import UI
from KnightJ import KnightJ
import Game_FrameWork
import Title_State



name = "Stage1"

stage1 = None
player = None
font = None
yeti = None
ui = None
knightJ = None
backgroundX = 0



class Stage1:
    backgroundX = 0

    def __init__(self):
        self.image = load_image('Stage1(1125x600).png')

    def draw(self):
        self.image.clip_draw(self.backgroundX, 0, 800, 780, 400, 300)
    def setBackgroundX(self, x):
        backgroundX = x



def enter():
    global stage1, player, yeti, ui, knightJ
    stage1 = Stage1()
    player = Player(340)
    yeti = Yeti()
    knightJ = KnightJ(player.x)
    ui = UI()

def exit():
    global stage1, yeti, player, knightJ
    del(yeti)
    del(stage1)
    del(player)
    del(knightJ)



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
    global player, yeti, knightJ, stage1
    stage1.setBackgroundX(backgroundX)
    player.update()
    player.setBackgroundX(backgroundX)
    yeti.update()
    yeti.setBackgroundX(backgroundX)
    yeti.setPlayerPos(player.x + backgroundX, player.y)
    knightJ.setBackgroundX(backgroundX)
    knightJ.setPlayerDir(player.dir)
    knightJ.setPlayerState( player.state )
    knightJ.update()
    scroll()



def draw():
    global stage1, player, yeti, knightJ

    clear_canvas()
    stage1.draw()
    ui.draw()
    ui.setPlayerHp(player.hp, player.maxHp)
    player.draw()
    knightJ.draw()
    yeti.draw()
    update_canvas()

# ----------------
def scroll():
# ----------------
    global backgroundX, player

    if player.state == player.WALK:
        if player.x >= 650:
            if backgroundX < 340:
                backgroundX += 20

        elif player.x <= 150:
            if backgroundX >= 20:
                backgroundX -= 20




