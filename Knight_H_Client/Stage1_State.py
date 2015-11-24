﻿import random
import json
import os

from pico2d import *
from Player import Player
from Yeti import Yeti
from UI import UI
from Lizard import Lizard
from Portal import Portal
import Game_FrameWork
import Title_State



name = "Stage1"

stage1 = None
player = None
font = None


yetiCount = 0
lizardCount = 0
yetiList = []
lizardList = []

ui = None
lizard = None
portal = None

lizardMpValue = 50
gemumuMpValue = 100
wizardMpValue = 200

lizardButton = False
gemumuButton = False
wizardButton = False


class Stage1:

    def __init__(self):
        self.image = load_image('Stage1(1125x600).png')
        self.backgroundX = 0

    def draw(self):
        self.image.clip_draw(self.backgroundX, 0, 800, 780, 400, 300)
    def setBackgroundX(self, x):
        self.backgroundX = x


        
def enter():
    global stage1, player, yetiList, ui, lizard, portal, yetiCount
    stage1 = Stage1()
    player = Player(340)
    lizard = Lizard(player.x)
    ui = UI()
    portal = Portal(1125, 200)

    for i in range(0, 2):
        yetiList.append(Yeti())
        yetiCount += 1

def exit():
    global stage1, player, portal
    del(stage1)
    del(player)
    del(portal)
    


def pause():
    pass


def resume():
    pass


def handle_events():
    global player, UI, lizardMpValue, gemumuMpValue, wizardMpValue, lizardList, lizardButton, lizardCount

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            Game_FrameWork.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
               Game_FrameWork.change_state(Title_State)
        elif (event.type) == SDL_MOUSEMOTION:
              if( 87 <= event.x and event.x <= 113 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - lizardMpValue > 0):
                      ui.LizardFrame = 27
                 else:
                     ui.LizardFrame = 54
              elif( 117 <= event.x and event.x <= 143 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - gemumuMpValue > 0):
                      ui.GemumuFrame = 27
                 else:
                     ui.GemumuFrame = 54
              elif( 147 <= event.x and event.x <= 173 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - wizardMpValue > 0):
                      ui.WizardFrame = 27
                 else:
                     ui.WizardFrame = 54
              else:
                  ui.LizardFrame = 0
                  ui.GemumuFrame = 0
                  ui.WizardFrame = 0

        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
              if( 87 <= event.x and event.x <= 113 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - lizardMpValue > 0):
                      lizardButton = True
                      print("리자드를 소환하시겠습니까?")
                 else:
                     ui.LizardFrame = 54
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
              if( 87 <= event.x and event.x <= 113 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - lizardMpValue > 0):
                      lizardButton = False
                      lizardList.append(Lizard(player.x))
                      print("리자드를 소환 합니다")
                      lizardCount += 1
                      player.mp -= lizardMpValue
                 
                               
        else:
           player.handle_events(event)

def update():
    global player, yetiList, lizardList, stage1, portal, yetiCount, lizardCount
    
    player.update()
    player.setBackgroundX(stage1.backgroundX)
    
    if( yetiCount > 0 ):
     for yeti in yetiList:
         yeti.update()
         yeti.setBackgroundX(stage1.backgroundX)
         yeti.setPlayerPos(player.x + stage1.backgroundX, player.y)

    
    if( lizardCount > 0 ):
     for lizard in lizardList:
         lizard.setBackgroundX(stage1.backgroundX)
         lizard.setPlayerState( player.state )
         lizard.setMonsterX( yeti.x )
         lizard.update()
    portal.setBackgroundX(stage1.backgroundX)
    
    scroll()
    collision()
    



def draw():
    global stage1, player, yetiList, lizardList, portal, yetiCount, lizardCount

    clear_canvas()
    stage1.draw()
    ui.draw()
    ui.setPlayerHp(player.hp, player.maxHp)
    
    player.draw()
    
    if( lizardCount > 0 ):
     for lizard in lizardList:
          lizard.draw()
    
    if( yetiCount > 0 ):
     for yeti in yetiList:
         yeti.draw()
    
    portal.draw()
    
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
def collide(a, b):
# ----------------
    left_a, top_a, right_a, bottom_a = a.get_bb()
    left_b, top_b, right_b, bottom_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    return True

# ----------------
def collision():
# ----------------
    global yetiCount, lizardList, yetiList, lizardCount, player

    if (lizardCount == 0):
        for yeti in yetiList:
            if( yeti.state != yeti.ATTACK and collide(player, yeti) ):
                yeti.state = yeti.ATTACK
                yeti.frame = 0
            elif( yeti.state == yeti.ATTACK and collide(player, yeti) and yeti.frame == yeti.frameNum[yeti.ATTACK] - 1):
                player.hp -= yeti.att
                print(player.hp)
            elif( yeti.state == yeti.ATTACK and True != collide(player, yeti) ):
                yeti.state = yeti.RUN