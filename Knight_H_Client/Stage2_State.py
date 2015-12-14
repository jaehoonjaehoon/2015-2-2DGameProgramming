import random
import json
import os

import time

from pico2d import *
from Player import Player
from Mermadia import Mermadia
from UI import UI
from Lizard import Lizard
from Gemumu import Gemumu
from Magician import Magician
from Portal import Portal
from Mermadia import Mermadia
import Game_FrameWork
import Stage3_State



name = "Stage2"

stage2 = None
player = None
font = None

storeCheck = False

mermadiaCount = 0
lizardCount = 0
gemumuCount = 0
magicianCount = 0

monsterZenTime = time.time()
monsterMaxZen = 5
monsterCurZen = 0

mermadiaCol = 0

mermadiaList = []
lizardList = []
gemumuList = []
magicianList = []

ui = None
portal = None
stage2Bgm = None
storeSound = None
lizardMpValue = 50
gemumuMpValue = 100
magicianMpValue = 200

lizardButton = False
gemumuButton = False
magicianButton = False


class Stage2:

    def __init__(self):
        self.image = load_image('Stage2(1125x600).png')
        self.backgroundX = 0

    def draw(self):
        self.image.clip_draw(self.backgroundX, 0, 800, 780, 400, 300)
    def setBackgroundX(self, x):
        self.backgroundX = x


        
def enter():
    global stage2, player, mermadiaList, ui, portal, mermadiaCount, stage2Bgm, storeSound
    stage2 = Stage2()
    player = Player(340)
    lizard = Lizard(player.x)
    ui = UI()
    portal = Portal(1125, 200)

    stage2Bgm = load_music('Stage2Bgm.mp3')
    stage2Bgm.set_volume(100)
    stage2Bgm.repeat_play()

    storeSound = load_wav('StoreSound.wav')
    storeSound.set_volume(64)

    f = open("stageInfoLoad.txt", 'r')
       
    data = f.readline()
    ui.money = int(data)
    
    data = f.readline()
    ui.score = int(data)
    f.close()

    for i in range(0, 14):
        mermadiaList.append(Mermadia())
        mermadiaCount += 1



def exit():
    global stage2, player, portal, lizardList, gemumuList, magicianList, mermadiaList, stage2Bgm
    del(stage2)
    del(player)
    del(portal)
    del(stage2Bgm)
    for lizard in lizardList:
        del(lizard)
    for gemumu in gemumuList:
        del(gemumu)
    for magician in magicianList:
        del(magician)
    for mermadia in mermadiaList:
        del(mermadia)
    


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
    global player, mermadiaList, lizardList, stage2, portal, mermadiaCount, lizardCount, gemumuList, magicianList
    
    player.update()
    player.setBackgroundX(stage2.backgroundX)
    
    if( mermadiaCount > 0 ):
     for mermadia in mermadiaList:
         mermadia.update()
         mermadia.setBackgroundX(stage2.backgroundX)
         mermadia.setPlayerPos(player.x + stage2.backgroundX, player.y)

    
    if( lizardCount > 0 ):
     for lizard in lizardList:
         lizard.setBackgroundX(stage2.backgroundX)
         lizard.setPlayerState( player.state )
         lizard.update()
    if( magicianCount > 0):
        for magician in magicianList:
            magician.setBackgroundX(stage2.backgroundX)
            magician.setPlayerState( player. state)
            magician.update()
    if( gemumuCount > 0):
        for gemumu in gemumuList:
            gemumu.setBackgroundX(stage2.backgroundX)
            gemumu.setPlayerState( player. state)
            gemumu.update()
    portal.setBackgroundX(stage2.backgroundX)
    
    ui.update()

    scroll()
    collision()
    dieCheck()
    stateCheck()



def draw():
    global stage2, player, mermadiaList, lizardList, portal, mermadiaCount, lizardCount, gemumuList, magicianList

    clear_canvas()
    stage2.draw()
    
    
    player.draw()
    
    if( lizardCount > 0 ):
     for lizard in lizardList:
          lizard.draw()
    if( gemumuCount > 0 ):
     for gemumu in gemumuList:
          gemumu.draw()
    if( mermadiaCount > 0 ):
     for mermadia in mermadiaList:
         mermadia.draw()
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
def collideDefend(a, b):
# ----------------
    left_a, top_a, right_a, bottom_a = a.get_bb_defend()
    left_b, top_b, right_b, bottom_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    return True
def monsterZen():

    global monsterZenTime, monsterMaxZen, monsterCurZen, mermadiaList, mermadiaCount

    
    if time.time() - monsterZenTime >= 8.0:
       if(monsterMaxZen > monsterCurZen):
           monsterZenTime = time.time()
           mermadiaList.append(mermadia())
           mermadiaCount += 1
           monsterCurZen += 1
# ----------------
def stateCheck():
# ----------------
    global mermadiaCount, lizardList, mermadiaList, lizardCount, player, portal, gemumuList, gemumuCount
    global magicianCount, magicianList
    lizardTomermadia = 0
    gemumuTomermadia = 0
    magicianTomermadia = 0
    mermadiaCheck = 0

    if(lizardCount > 0 and mermadiaCount > 0 ):
        for mermadia in mermadiaList:
            for lizard in lizardList:
                if(lizard.state == lizard.ATTACK and collide(mermadia, lizard) == True):
                    lizardTomermadia += 1
                 
        for mermadia in mermadiaList:
            for lizard in lizardList:
                if(lizard.state == lizard.ATTACK and collide(mermadia, lizard) == False and lizardTomermadia == 0):
                    lizard.state = lizard.RUN

    if(magicianCount > 0 and mermadiaCount > 0 ):
        for mermadia in mermadiaList:
            for magician in magicianList:
                if(magician.state == magician.ATTACK and collide(magician, mermadia) == True):
                    magicianTomermadia += 1
        for mermadia in mermadiaList:
            for magician in magicianList:
                if(magician.state == magician.ATTACK and collide(magician, mermadia) == False and magicianTomermadia == 0):
                    magician.state = magician.RUN 

    if(gemumuCount > 0 and mermadiaCount > 0 ):
        for mermadia in mermadiaList:
            for gemumu in gemumuList:
                if(gemumu.state == gemumu.ATTACK and collide(gemumu, mermadia) == True):
                    gemumuTomermadia += 1
        for mermadia in mermadiaList:
            for gemumu in gemumuList:
                if(gemumu.state == gemumu.ATTACK and collide(gemumu, mermadia) == False and gemumuTomermadia == 0):
                    gemumu.state = gemumu.RUN  


    if(gemumuCount > 0 or magicianCount > 0 or lizardCount > 0 and mermadiaCount > 0):
        for mermadia in mermadiaList:
            for lizard in lizardList:
                if(mermadia.state == mermadia.ATTACK and collide(lizard, mermadia) == True):
                    mermadiaCheck += 1
        for mermadia in mermadiaList:
            for lizard in lizardList:
                if(mermadia.state == mermadia.ATTACK and collide(lizard, mermadia) == False and mermadiaCheck == 0 ):
                    mermadia.state = mermadia.RUN  


        for mermadia in mermadiaList:
            for magician in magicianList:
                if(mermadia.state == mermadia.ATTACK and collideDefend(magician, mermadia) == True):
                    mermadiaCheck += 1                  
        for mermadia in mermadiaList:
            for magician in magicianList:
                if(mermadia.state == mermadia.ATTACK and collideDefend(magician, mermadia) == False and mermadiaCheck == 0):
                    mermadia.state = mermadia.RUN


        for mermadia in mermadiaList:
            for gemumu in gemumuList:
                if(mermadia.state == mermadia.ATTACK and collideDefend(gemumu, mermadia) == True):
                    mermadiaCheck += 1
        for mermadia in mermadiaList:
            for gemumu in gemumuList:
                if(mermadia.state == mermadia.ATTACK and collideDefend(gemumu, mermadia) == False and mermadiaCheck == 0):
                    mermadia.state = mermadia.RUN 
# ----------------
def dieCheck():
# ----------------
    global mermadiaCount, lizardList, mermadiaList, lizardCount, player, portal, gemumuList, gemumuCount
    global magicianCount, magicianList, ui

    for mermadia in mermadiaList:
        if(mermadia.state == mermadia.DIE and mermadia.frame == mermadia.frameNum[mermadia.DIE]-1):
                            mermadiaCount -= 1
                            mermadia.frame = 0
                            mermadiaList.remove(mermadia)
                            ui.score += random.randint(2000, 4000)
                            ui.money += random.randint(800, 1800)
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
    global mermadiaCount, lizardList, mermadiaList, lizardCount, player, portal, gemumuList, gemumuCount
    global magicianCount, magicianList, ui
    
    if collide(portal, player) and mermadiaCount == 0:
        f = open("stageInfoLoad.txt", 'w')
       
        data = "%d " % ui.money
        f.write(data) 
        data = "%d " % ui.score
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
        for mermadia in mermadiaList:
            if( mermadia.state != mermadia.ATTACK and collide(player, mermadia) and player.state != player.DIE ):
                mermadia.state = mermadia.ATTACK
                mermadia.frame = 0
            elif( mermadia.state == mermadia.ATTACK and collide(player, mermadia) and mermadia.frame == mermadia.frameNum[mermadia.ATTACK] - 1):
                player.hp -= mermadia.att
                mermadia.frame = 0
                print(player.hp)
            elif( mermadia.state == mermadia.ATTACK and True != collide(player, mermadia) ):
                mermadia.state = mermadia.RUN
                mermadia.frame = 0

    if( mermadiaCount == 0):
        for lizard in lizardList:
            lizard.state = lizard.RUN
        for magician in magicianList:
            magician.state = magician.RUN
        for gemumu in gemumuList:
            gemumu.state = gemumu.RUN

    if( mermadiaCount > 0 and lizardCount > 0):
        for mermadia in mermadiaList:
            for lizard in lizardList:
                if( collide(lizard, mermadia) == True ):
                    if(lizard.state == lizard.RUN):
                        lizard.state = lizard.ATTACK
                        lizard.frame = 0
                    elif(lizard.state == lizard.ATTACK):
                        if(lizard.frame == lizard.frameNum[lizard.ATTACK]-1):
                           mermadia.hp -= lizard.att
                           lizard.frame = 0
                           print("mermadia hp : ", mermadia.hp)

                    if(mermadia.state == mermadia.STAND or mermadia.state == mermadia.RUN):
                        mermadia.state = mermadia.ATTACK
                        mermadia.frame = 0
                    elif(mermadia.state == mermadia.ATTACK):
                        if(mermadia.frame == mermadia.frameNum[mermadia.ATTACK]-1):
                            lizard.hp -= mermadia.att
                            mermadia.frame = 0
                            print("lizard hp : ", lizard.hp)
                    
     
    if( gemumuCount > 0 and mermadiaCount > 0):
        for mermadia in mermadiaList:
           for gemumu in gemumuList:
                if( collide(gemumu, mermadia) == True ):
                    if(gemumu.state == gemumu.RUN):
                        if( gemumu.waveState == 0 ):
                            gemumu.setMonsterX(mermadia.x)
                            gemumu.createEnergyWave()
                            gemumu.state = gemumu.ATTACK
                    elif(gemumu.state == gemumu.ATTACK):
                        if( gemumu.waveState == 0 ):
                            gemumu.setMonsterX(mermadia.x)
                            gemumu.createEnergyWave()
                        if(gemumu.frame == gemumu.frameNum[gemumu.ATTACK]-1):
                            mermadia.hp -= gemumu.att
                            gemumu.frame = 0
                            print("mermadia hp : ", mermadia.hp)

                if( collideDefend(gemumu, mermadia) == True ):
                    if(mermadia.state == mermadia.STAND or mermadia.state == mermadia.RUN):
                        mermadia.state = mermadia.ATTACK
                        mermadia.frame = 0
                    elif(mermadia.state == mermadia.ATTACK):
                        if(mermadia.frame == mermadia.frameNum[mermadia.ATTACK]-1):
                            gemumu.hp -= mermadia.att
                            mermadia.frame = 0
                            print("gemumu hp : ", gemumu.hp)

    if( magicianCount > 0 and mermadiaCount > 0):
        for mermadia in mermadiaList:
           for magician in magicianList:
                if( collide(magician, mermadia) == True ):
                    if(magician.state == magician.RUN):
                        if( magician.fireState == 0 ):
                            magician.createFire(mermadia.x, mermadia.y)
                            magician.state = magician.ATTACK
                    elif(magician.state == magician.ATTACK):
                        if( magician.fireState == 0 ):
                            magician.createFire(mermadia.x, mermadia.y)
                            magician.state = magician.ATTACK
                        if(magician.frame == magician.frameNum[magician.ATTACK]-1):
                            mermadia.hp -= magician.att
                            magician.frame = 0
                            print("mermadia hp : ", mermadia.hp)

                if( collideDefend(magician, mermadia) == True ):
                    if(mermadia.state == mermadia.STAND or mermadia.state == mermadia.RUN):
                        mermadia.state = mermadia.ATTACK
                        mermadia.frame = 0
                    elif(mermadia.state == mermadia.ATTACK):
                        if(mermadia.frame == mermadia.frameNum[mermadia.ATTACK]-1):
                            magician.hp -= mermadia.att
                            mermadia.frame = 0
                            print("magician hp : ", magician.hp)
