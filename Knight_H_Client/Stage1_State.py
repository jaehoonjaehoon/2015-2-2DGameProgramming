import random
import json
import os

from pico2d import *
from Player import Player
from Yeti import Yeti
from UI import UI
from Lizard import Lizard
from Gemumu import Gemumu
from Magician import Magician
from Portal import Portal
import Game_FrameWork
import Title_State
import Stage2_State




name = "Stage1"

stage1 = None
player = None
font = None


yetiCount = 0
lizardCount = 0
gemumuCount = 0
magicianCount = 0

yetiList = []
lizardList = []
gemumuList = []
magicianList = []

ui = None
portal = None
stage1Bgm = None

lizardMpValue = 50
gemumuMpValue = 100
magicianMpValue = 200

lizardButton = False
gemumuButton = False
magicianButton = False


class Stage1:

    def __init__(self):
        self.image = load_image('Stage1(1125x600).png')
        self.backgroundX = 0

    def draw(self):
        self.image.clip_draw(self.backgroundX, 0, 800, 780, 400, 300)
    def setBackgroundX(self, x):
        self.backgroundX = x


        
def enter():
    global stage1, player, yetiList, ui, portal, yetiCount, stage1Bgm
    stage1 = Stage1()
    player = Player(340)
    lizard = Lizard(player.x)
    ui = UI()
    portal = Portal(1125, 200)

    stage1Bgm = load_music('stage1Bgm.mp3')
    stage1Bgm.set_volume(100)
    stage1Bgm.repeat_play()

    for i in range(0, 3):
        yetiList.append(Yeti())
        yetiCount += 1

def exit():
    global stage1, player, portal, lizardList, gemumuList, magicianList, yetiList, stage1Bgm
    del(stage1)
    del(player)
    del(portal)
    del(stage1Bgm)
    for lizard in lizardList:
        del(lizard)
    for gemumu in gemumuList:
        del(gemumu)
    for magician in magicianList:
        del(magician)
    for yeti in yetiList:
        del(yeti)
    


def pause():
    pass


def resume():
    pass


def handle_events():
    global player, UI, lizardMpValue, gemumuMpValue, magicianMpValue, lizardList, lizardButton, lizardCount
    global gemumuList, magicianList, magicianButton, gemumuButton, gemumuCount, magicianCount
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            Game_FrameWork.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
               Game_FrameWork.change_state(Title_State)
        elif (event.type) == SDL_MOUSEMOTION:
              if(87 <= event.x and event.x <= 113 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - lizardMpValue > 0):
                      ui.LizardFrame = 27
                 else:
                     ui.LizardFrame = 54
              elif(117 <= event.x and event.x <= 143 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - gemumuMpValue > 0):
                      ui.GemumuFrame = 27
                 else:
                     ui.GemumuFrame = 54
              elif(147 <= event.x and event.x <= 173 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - magicianMpValue > 0):
                      ui.MagicianFrame = 27
                 else:
                     ui.Magician = 54
              else:
                  ui.LizardFrame = 0
                  ui.GemumuFrame = 0
                  ui.MagicianFrame = 0
        
         #UI 위에 마우스를 올려놓은상태에서 왼쪽 버튼을 DOWN 했을경우
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
              if(87 <= event.x and event.x <= 113 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - lizardMpValue > 0):
                      lizardButton = True
                 else:
                     ui.LizardFrame = 54
              elif(117 <= event.x and event.x <= 143 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - gemumuMpValue > 0):
                      gemumuButton = True
                 else:
                     ui.GemumuFrame = 54
              elif(147 <= event.x and event.x <= 173 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - magicianMpValue > 0):
                      magicianButton = True
                 else:
                     ui.MagicianFrame = 54

        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
              if(87 <= event.x and event.x <= 113 and 18 <= 600 - event.y and 600 - event.y <= 58):
                 if(player.mp - lizardMpValue > 0):
                      lizardButton = False
                      lizardList.append(Lizard(player.x))
                      lizardCount += 1
                      player.mp -= lizardMpValue
              elif(117 <= event.x and event.x <= 143 and 18 <= 600 - event.y and 600 - event.y <= 58):
                  if(player.mp - gemumuMpValue > 0):
                      gemumuButton = False
                      gemumuList.append(Gemumu(player.x))
                      gemumuCount += 1
                      player.mp -= gemumuMpValue
              elif(147 <= event.x and event.x <= 173 and 18 <= 600 - event.y and 600 - event.y <= 58):
                  if(player.mp - magicianMpValue > 0):
                      magicianButton = False
                      magicianList.append(Magician(player.x))
                      magicianCount += 1
                      player.mp -= magicianMpValue
                               
        else:
           player.handle_events(event)

def update():
    global player, yetiList, lizardList, stage1, portal, yetiCount, lizardCount, gemumuList, magicianList
    
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
         lizard.update()
    if( magicianCount > 0):
        for magician in magicianList:
            magician.setBackgroundX(stage1.backgroundX)
            magician.setPlayerState( player. state)
            magician.update()
    if( gemumuCount > 0):
        for gemumu in gemumuList:
            gemumu.setBackgroundX(stage1.backgroundX)
            gemumu.setPlayerState( player. state)
            gemumu.update()
    portal.setBackgroundX(stage1.backgroundX)
    
    scroll()
    collision()
    



def draw():
    global stage1, player, yetiList, lizardList, portal, yetiCount, lizardCount, gemumuList, magicianList

    clear_canvas()
    stage1.draw()
    ui.draw()
    ui.setPlayerHp(player.hp, player.maxHp)
    
    player.draw()
    
    if( lizardCount > 0 ):
     for lizard in lizardList:
          lizard.draw()
    if( gemumuCount > 0 ):
     for gemumu in gemumuList:
          gemumu.draw()
    if( magicianCount > 0 ):
     for magician in magicianList:
          magician.draw()
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
    global yetiCount, lizardList, yetiList, lizardCount, player, portal, gemumuList, gemumuCount
    global magicianCount, magicianList
    
    if collide(portal, player):
        Game_FrameWork.change_state(Stage2_State)
        return

    if (lizardCount == 0 and gemumuCount == 0 and magicianCount == 0 ):
        for yeti in yetiList:
            if( yeti.state != yeti.ATTACK and collide(player, yeti) and player.state != player.DIE ):
                yeti.state = yeti.ATTACK
                yeti.frame = 0
            elif( yeti.state == yeti.ATTACK and collide(player, yeti) and yeti.frame == yeti.frameNum[yeti.ATTACK] - 1):
                player.hp -= yeti.att
                yeti.frame = 0
                print(player.hp)
            elif( yeti.state == yeti.ATTACK and True != collide(player, yeti) ):
                yeti.state = yeti.RUN
                yeti.frame = 0


    elif ( lizardCount > 0 and yetiCount > 0 ):
        for yeti in yetiList:
            for lizard in lizardList:
                if( collide(lizard, yeti) == True ):
                    if( yeti.state == yeti.RUN):
                         yeti.state = yeti.ATTACK
                         yeti.frame = 0
                    elif( yeti.state == yeti.ATTACK):
                        if( yeti.frame == yeti.frameNum[yeti.ATTACK]-1 and lizard.state != lizard.DIE):
                            lizard.hp -= yeti.att
                            yeti.frame = 0
                            print( "lizard의 Hp : ",lizard.hp )
                    if(lizard.hp <= 0):
                        lizard.state = lizard.DIE
                    elif( yeti.state == yeti.DIE and yeti.frame == yeti.frameNum[yeti.DIE]-1):
                            yeti.frame = 0
                            yetiCount -= 1
                            yetiList.remove(yeti)                          
                    if( lizard.state == lizard.RUN):
                         lizard.state = lizard.ATTACK
                    elif( lizard.state == lizard.ATTACK):
                        if( lizard.frame == lizard.frameNum[lizard.ATTACK]-1 and yeti.state != yeti.DIE):
                            yeti.hp -= lizard.att
                            lizard.frame = 0
                            print( "yeti의 Hp", yeti.hp)
                    if(yeti.hp <= 0):
                           yeti.state = yeti.DIE
                    elif( lizard.state == lizard.DIE and lizard.frame == lizard.frameNum[lizard.DIE]-1 ):
                            lizardCount -= 1
                            lizardList.remove(lizard)
                elif( collide(lizard, yeti) == False):
                       lizard.state = lizard.RUN

    elif ( yetiCount <= 0 ):  
         for lizard in lizardList:
             lizard.state = lizard.RUN
         