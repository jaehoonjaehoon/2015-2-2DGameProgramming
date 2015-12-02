import random
import json
import os

from pico2d import *
from Player import Player
from Yeti import Yeti
from UI import UI
from Lizard import Lizard
from Portal import Portal
import Game_FrameWork
import Stage1_State
import Stage3_State


name = "Stage2"

stage2 = None
player = None
font = None


yetiCount = 0
lizardCount = 0
yetiList = []
lizardList = []

ui = None
lizard = None
portal = None
stage2Bgm = None


lizardMpValue = 50
gemumuMpValue = 100
wizardMpValue = 200

lizardButton = False
gemumuButton = False
wizardButton = False



class Stage2:

    def __init__(self):
        self.image = load_image('Stage2(1125x600).png')
        self.backgroundX = 0

    def draw(self):
        self.image.clip_draw(self.backgroundX, 0, 800, 780, 400, 300)
    def setBackgroundX(self, x):
        self.backgroundX = x


        
def enter():
    global stage2, player, yetiList, ui, lizard, portal, yetiCount, stage2Bgm
    stage2 = Stage2()
    player = Player(340)
    lizard = Lizard(player.x)
    ui = UI()
    portal = Portal(1125, 200)

    stage2Bgm = load_music('stage2Bgm.mp3')
    stage2Bgm.set_volume(100)
    stage2Bgm.repeat_play()

    for i in range(0, 15):
        yetiList.append(Yeti())
        yetiCount += 1

def exit():
    global stage2, player, portal, lizardList, yetiList, stage2Bgm
    del(stage2)
    del(player)
    del(portal)
    del(stage2Bgm)
    for lizard in lizardList:
        del(lizard)
    for yeti in yetiList:
        del(yeti)
    


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
               Game_FrameWork.change_state(Stage1_State)
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
                 else:
                     ui.LizardFrame = 54
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
              if( 87 <= event.x and event.x <= 113 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - lizardMpValue > 0):
                      lizardButton = False
                      lizardList.append(Lizard(player.x))
                      lizardCount += 1
                      player.mp -= lizardMpValue
                 
                               
        else:
           player.handle_events(event)

def update():
    global player, yetiList, lizardList, stage2, portal, yetiCount, lizardCount
    
    player.update()
    player.setBackgroundX(stage2.backgroundX)
    
    if( yetiCount > 0 ):
     for yeti in yetiList:
         yeti.update()
         yeti.setBackgroundX(stage2.backgroundX)
         yeti.setPlayerPos(player.x + stage2.backgroundX, player.y)

    
    if( lizardCount > 0 ):
     for lizard in lizardList:
         lizard.setBackgroundX(stage2.backgroundX)
         lizard.setPlayerState( player.state )
         #lizard.setMonsterX( yeti.x )
         lizard.update()
    portal.setBackgroundX(stage2.backgroundX)
    
    scroll()
    collision()
    



def draw():
    global stage2, player, yetiList, lizardList, portal, yetiCount, lizardCount

    clear_canvas()
    stage2.draw()
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
    global stage2, player

    if player.state == player.WALK:
        if player.x >= 640:
            if stage2.backgroundX < 340:
                stage2.backgroundX += 5
        elif player.x <= 150:
            if stage2.backgroundX >= 20:
                stage2.backgroundX -= 5

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
    global yetiCount, lizardList, yetiList, lizardCount, player, portal

    if collide(portal, player):
        Game_FrameWork.change_state(Stage3_State)
        return

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
    elif ( lizardCount > 0 and yetiCount > 0 ):
        for yeti in yetiList:
            for lizard in lizardList:
                if( collide(lizard, yeti) == True ):
                    if( yeti.state == yeti.RUN):
                         yeti.state = yeti.ATTACK
                         yeti.frame = 0
                    elif( yeti.state == yeti.ATTACK and yeti.frame == yeti.frameNum[yeti.ATTACK]-1 ):
                        lizard.hp -= yeti.att
                        if( lizard.hp <= 0 and lizard.state == lizard.DIE and lizard.frame == lizard.frameNum[lizard.DIE]-1):
                            lizardList.remove(lizard)
                            lizardCount -= 1
                        elif( lizard.hp <= 0 and lizard.state != lizard.DIE):
                            lizard.state = lizard.DIE
                            lizard.frame = 0

                    if( lizard.state == lizard.RUN):
                         lizard.state = lizard.ATTACK
                         lizard.frame = 0
                    elif( lizard.state == lizard.ATTACK and lizard.frame == lizard.frameNum[lizard.ATTACK]-1  ):
                        yeti.hp -= lizard.att
                        #print("yeti�� HP : ", yeti.hp)
                        if( yeti.hp <= 0 and yeti.state == yeti.DIE and yeti.frame == yeti.frameNum[yeti.DIE]-1):
                            yetiCount -= 1
                        elif( yeti.hp <= 0 and yeti.state != yeti.DIE):
                            yeti.state = yeti.DIE
                            yeti.frame = 0
    elif(yetiCount <= 0):
        for lizard in lizardList:
            lizard.state = lizard.RUN
         