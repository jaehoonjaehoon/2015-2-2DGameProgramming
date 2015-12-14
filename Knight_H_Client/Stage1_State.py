import random
import json
import os

import time

from pico2d import *
from Player import Player
from Yeti import Yeti
from UI import UI
from Lizard import Lizard
from Gemumu import Gemumu
from Magician import Magician
from Portal import Portal
from Mermadia import Mermadia
import Game_FrameWork
import Title_State
import Stage2_State



name = "Stage1"

stage1 = None
player = None
font = None

storeCheck = False

yetiCount = 0
lizardCount = 0
gemumuCount = 0
magicianCount = 0

monsterZenTime = time.time()
monsterMaxZen = 5
monsterCurZen = 0

yetiCol = 0

yetiList = []
lizardList = []
gemumuList = []
magicianList = []

ui = None
portal = None
stage1Bgm = None
storeSound = None
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
    global stage1, player, yetiList, ui, portal, yetiCount, stage1Bgm, storeSound
    stage1 = Stage1()
    player = Player(340)
    lizard = Lizard(player.x)
    ui = UI()
    portal = Portal(1125, 200)

    stage1Bgm = load_music('stage1Bgm.mp3')
    stage1Bgm.set_volume(100)
    stage1Bgm.repeat_play()

    storeSound = load_wav('StoreSound.wav')
    storeSound.set_volume(64)

    for i in range(0, 11):
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
    global gemumuList, magicianList, magicianButton, gemumuButton, gemumuCount, magicianCount, storeSound
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            Game_FrameWork.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
               Game_FrameWork.change_state(Title_State)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_i):

            storeSound.play()

            if(ui.storeCheck == False):    
                ui.storeCheck = True
            else:
                ui.storeCheck = False

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
              if(player.mp - lizardMpValue > 0 and ui.storeCheck == False):
                 lizardList.append(Lizard(player.x))
                 lizardCount += 1
                 player.mp -= lizardMpValue
              elif(ui.storeCheck == True and ui.money > 100 ):
                 ui.money -= 100
                 for lizard in lizardList:
                     lizard.maxHp += 100
                     lizard.hp = lizard.maxHp

                 
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_2):
              if(player.mp - gemumuMpValue > 0 and ui.storeCheck == False):
                  gemumuList.append(Gemumu(player.x))
                  gemumuCount += 1
                  player.mp -= gemumuMpValue
              elif(ui.storeCheck == True and ui.money > 200 ):
                 ui.money -= 200
                 for gemumu in gemumuList:
                     gemumu.maxHp += 100
                     gemumu.hp = gemumu.maxHp

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_3):
              if(player.mp - magicianMpValue > 0 and ui.storeCheck == False):
                  magicianList.append(Magician(player.x))
                  magicianCount += 1
                  player.mp -= magicianMpValue
              elif(ui.storeCheck == True and ui.money > 400 ):
                 ui.money -= 400
                 for magician in magicianList:
                     magician.maxHp += 100
                     magician.hp = magician.maxHp
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_4):
            if(ui.storeCheck == True and ui.money > 100 ):
                 ui.money -= 100
                 for lizard in lizardList:
                     lizard.att += 50
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_5):
            if(ui.storeCheck == True and ui.money > 200 ):
                 ui.money -= 200
                 for gemumu in gemumuList:
                     gemumu.att += 50
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_6):
            if(ui.storeCheck == True and ui.money > 300 ):
                 ui.money -= 300
                 for magician in magicianList:
                     magician.att += 50
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
                     ui.MagicianFrame = 54
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
    
    ui.update()

    scroll()
    collision()
    dieCheck()
    stateCheck()



def draw():
    global stage1, player, yetiList, lizardList, portal, yetiCount, lizardCount, gemumuList, magicianList

    clear_canvas()
    stage1.draw()
    
    
    player.draw()
    
    if( lizardCount > 0 ):
     for lizard in lizardList:
          lizard.draw()
    if( gemumuCount > 0 ):
     for gemumu in gemumuList:
          gemumu.draw()
    if( yetiCount > 0 ):
     for yeti in yetiList:
         yeti.draw()
    if( magicianCount > 0 ):
     for magician in magicianList:
          magician.draw()
    portal.draw()

    ui.draw()
    ui.drawPlayerHp(player.hp, player.maxHp)
    ui.drawPlayerMp(player.mp, player.maxMp)

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
def collideDefend(a, b):
# ----------------
    left_a, top_a, right_a, bottom_a = a.get_bb_defend()
    left_b, top_b, right_b, bottom_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    return True
def monsterZen():

    global monsterZenTime, monsterMaxZen, monsterCurZen, yetiList, yetiCount

    
    if time.time() - monsterZenTime >= 8.0:
       if(monsterMaxZen > monsterCurZen):
           monsterZenTime = time.time()
           yetiList.append(Yeti())
           yetiCount += 1
           monsterCurZen += 1
# ----------------
def stateCheck():
# ----------------
    global yetiCount, lizardList, yetiList, lizardCount, player, portal, gemumuList, gemumuCount
    global magicianCount, magicianList
    lizardToyeti = 0
    gemumuToyeti = 0
    magicianToyeti = 0
    yetiCheck = 0

    if(lizardCount > 0 and yetiCount > 0 ):
        for yeti in yetiList:
            for lizard in lizardList:
                if(lizard.state == lizard.ATTACK and collide(yeti, lizard) == True):
                    lizardToyeti += 1
                 
        for yeti in yetiList:
            for lizard in lizardList:
                if(lizard.state == lizard.ATTACK and collide(yeti, lizard) == False and lizardToyeti == 0):
                    lizard.state = lizard.RUN

    if(magicianCount > 0 and yetiCount > 0 ):
        for yeti in yetiList:
            for magician in magicianList:
                if(magician.state == magician.ATTACK and collide(magician, yeti) == True):
                    magicianToyeti += 1
        for yeti in yetiList:
            for magician in magicianList:
                if(magician.state == magician.ATTACK and collide(magician, yeti) == False and magicianToyeti == 0):
                    magician.state = magician.RUN 

    if(gemumuCount > 0 and yetiCount > 0 ):
        for yeti in yetiList:
            for gemumu in gemumuList:
                if(gemumu.state == gemumu.ATTACK and collide(gemumu, yeti) == True):
                    gemumuToyeti += 1
        for yeti in yetiList:
            for gemumu in gemumuList:
                if(gemumu.state == gemumu.ATTACK and collide(gemumu, yeti) == False and gemumuToyeti == 0):
                    gemumu.state = gemumu.RUN  


    if(gemumuCount > 0 or magicianCount > 0 or lizardCount > 0 and yetiCount > 0):
        for yeti in yetiList:
            for lizard in lizardList:
                if(yeti.state == yeti.ATTACK and collide(lizard, yeti) == True):
                    yetiCheck += 1
        for yeti in yetiList:
            for lizard in lizardList:
                if(yeti.state == yeti.ATTACK and collide(lizard, yeti) == False and yetiCheck == 0 ):
                    yeti.state = yeti.RUN  


        for yeti in yetiList:
            for magician in magicianList:
                if(yeti.state == yeti.ATTACK and collideDefend(magician, yeti) == True):
                    yetiCheck += 1                  
        for yeti in yetiList:
            for magician in magicianList:
                if(yeti.state == yeti.ATTACK and collideDefend(magician, yeti) == False and yetiCheck == 0):
                    yeti.state = yeti.RUN


        for yeti in yetiList:
            for gemumu in gemumuList:
                if(yeti.state == yeti.ATTACK and collideDefend(gemumu, yeti) == True):
                    yetiCheck += 1
        for yeti in yetiList:
            for gemumu in gemumuList:
                if(yeti.state == yeti.ATTACK and collideDefend(gemumu, yeti) == False and yetiCheck == 0):
                    yeti.state = yeti.RUN 
# ----------------
def dieCheck():
# ----------------
    global yetiCount, lizardList, yetiList, lizardCount, player, portal, gemumuList, gemumuCount
    global magicianCount, magicianList, ui

    for yeti in yetiList:
        if(yeti.state == yeti.DIE and yeti.frame == yeti.frameNum[yeti.DIE]-1):
                            yetiCount -= 1
                            yeti.frame = 0
                            yetiList.remove(yeti)
                            ui.score += random.randint(500, 1500)
                            ui.money += random.randint(300, 800)
    for lizard in lizardList:
        if(lizard.state == lizard.DIE and lizard.frame == lizard.frameNum[lizard.DIE]-1):
                            lizardCount -= 1
                            lizard.frame = 0
                            lizardList.remove(lizard)
    for gemumu in gemumuList:
        if(gemumu.state == gemumu.DIE and gemumu.frame == gemumu.frameNum[gemumu.DIE]-1):
                            gemumuCount -= 1
                            gemumu.frame = 0
                            gemumuList.remove(gemumu)
    for magician in magicianList:
        if(magician.state == magician.DIE and magician.frame == magician.frameNum[magician.DIE]-1):
                            magicianCount -= 1
                            magician.frame = 0
                            magicianList.remove(magician)
# ----------------
def collision():
# ----------------
    global yetiCount, lizardList, yetiList, lizardCount, player, portal, gemumuList, gemumuCount
    global magicianCount, magicianList, ui
    
    if collide(portal, player) and yetiCount == 0:
        f = open("stageInfoLoad.txt", 'w')
       
        data = "%d\n" % ui.money
        f.write(data) 
        data = "%d\n" % ui.score
        f.write(data)
        f.close()

        if lizardCount > 0:
            for lizard in lizardList:
                lizardList.remove(lizard)
                lizardCount -=1
        if gemumuCount > 0:
            for gemumu in gemumuList:
                gemumuList.remove(gemumu)
                gemumuCount -=1
        if magicianCount > 0:
            for magician in magicianList:
                magicianList.remove(magician)
                magicianCount -=1

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

    if( yetiCount == 0):
        for lizard in lizardList:
            lizard.state = lizard.RUN
        for magician in magicianList:
            magician.state = magician.RUN
        for gemumu in gemumuList:
            gemumu.state = gemumu.RUN

    if( yetiCount > 0 and lizardCount > 0):
        for yeti in yetiList:
            for lizard in lizardList:
                if( collide(lizard, yeti) == True ):
                    if(lizard.state == lizard.RUN):
                        lizard.state = lizard.ATTACK
                        lizard.frame = 0
                    elif(lizard.state == lizard.ATTACK):
                        if(lizard.frame == lizard.frameNum[lizard.ATTACK]-1):
                           yeti.hp -= lizard.att
                           lizard.frame = 0
                           print("yeti hp : ", yeti.hp)

                    if(yeti.state == yeti.STAND or yeti.state == yeti.RUN):
                        yeti.state = yeti.ATTACK
                        yeti.frame = 0
                    elif(yeti.state == yeti.ATTACK):
                        if(yeti.frame == yeti.frameNum[yeti.ATTACK]-1):
                            lizard.hp -= yeti.att
                            yeti.frame = 0
                            print("lizard hp : ", lizard.hp)
                    
     
    if( gemumuCount > 0 and yetiCount > 0):
        for yeti in yetiList:
           for gemumu in gemumuList:
                if( collide(gemumu, yeti) == True ):
                    if(gemumu.state == gemumu.RUN):
                        if( gemumu.waveState == 0 ):
                            gemumu.setMonsterX(yeti.x)
                            gemumu.createEnergyWave()
                            gemumu.state = gemumu.ATTACK
                    elif(gemumu.state == gemumu.ATTACK):
                        if( gemumu.waveState == 0 ):
                            gemumu.setMonsterX(yeti.x)
                            gemumu.createEnergyWave()
                        if(gemumu.frame == gemumu.frameNum[gemumu.ATTACK]-1):
                            yeti.hp -= gemumu.att
                            gemumu.frame = 0
                            print("yeti hp : ", yeti.hp)

                if( collideDefend(gemumu, yeti) == True ):
                    if(yeti.state == yeti.STAND or yeti.state == yeti.RUN):
                        yeti.state = yeti.ATTACK
                        yeti.frame = 0
                    elif(yeti.state == yeti.ATTACK):
                        if(yeti.frame == yeti.frameNum[yeti.ATTACK]-1):
                            gemumu.hp -= yeti.att
                            yeti.frame = 0
                            print("gemumu hp : ", gemumu.hp)

    if( magicianCount > 0 and yetiCount > 0):
        for yeti in yetiList:
           for magician in magicianList:
                if( collide(magician, yeti) == True ):
                    if(magician.state == magician.RUN):
                        if( magician.fireState == 0 ):
                            magician.createFire(yeti.x, yeti.y)
                            magician.state = magician.ATTACK
                    elif(magician.state == magician.ATTACK):
                        if( magician.fireState == 0 ):
                            magician.createFire(yeti.x, yeti.y)
                            magician.state = magician.ATTACK
                        if(magician.frame == magician.frameNum[magician.ATTACK]-1):
                            yeti.hp -= magician.att
                            magician.frame = 0
                            print("yeti hp : ", yeti.hp)

                if( collideDefend(magician, yeti) == True ):
                    if(yeti.state == yeti.STAND or yeti.state == yeti.RUN):
                        yeti.state = yeti.ATTACK
                        yeti.frame = 0
                    elif(yeti.state == yeti.ATTACK):
                        if(yeti.frame == yeti.frameNum[yeti.ATTACK]-1):
                            magician.hp -= yeti.att
                            yeti.frame = 0
                            print("magician hp : ", magician.hp)
