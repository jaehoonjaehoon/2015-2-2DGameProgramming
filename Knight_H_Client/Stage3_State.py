import random
import json
import os

import time

from pico2d import *
from Player import Player
from Dragon import Dragon
from UI import UI
from Lizard import Lizard
from Gemumu import Gemumu
from Magician import Magician
from Portal import Portal
import Game_FrameWork
import Title_State
import Stage3_State



name = "stage3"

stage3 = None
player = None
font = None

storeCheck = False

dragonCount = 0
lizardCount = 0
gemumuCount = 0
magicianCount = 0

monsterZenTime = time.time()
monsterMaxZen = 5
monsterCurZen = 0

dragonCol = 0

dragonList = []
lizardList = []
gemumuList = []
magicianList = []

ui = None
portal = None
stage3Bgm = None
storeSound = None
lizardMpValue = 50
gemumuMpValue = 100
magicianMpValue = 200

lizardButton = False
gemumuButton = False
magicianButton = False


class Stage3:

    def __init__(self):
        self.image = load_image('Stage3(1125x600).png')
        self.backgroundX = 0

    def draw(self):
        self.image.clip_draw(self.backgroundX, 0, 800, 780, 400, 300)
    def setBackgroundX(self, x):
        self.backgroundX = x


        
def enter():
    global stage3, player, dragonList, ui, portal, dragonCount, stage3Bgm, storeSound
    stage3 = Stage3()
    player = Player(340)
    lizard = Lizard(player.x)
    ui = UI()
    portal = Portal(1125, 200)

    stage3Bgm = load_music('Stage3Bgm.mp3')
    stage3Bgm.set_volume(100)
    stage3Bgm.repeat_play()

    storeSound = load_wav('StoreSound.wav')
    storeSound.set_volume(64)

    f = open("stageInfoLoad.txt", 'r')
       
    data = f.readline()
    ui.money = int(data)
    
    data = f.readline()
    ui.score = int(data)
    f.close()

    for i in range(0, 1):
        dragonList.append(Dragon())
        dragonCount += 1



def exit():
    global stage3, player, portal, lizardList, gemumuList, magicianList, dragonList, stage3Bgm
    del(stage3)
    del(player)
    del(portal)
    del(stage3Bgm)
    for lizard in lizardList:
        del(lizard)
    for gemumu in gemumuList:
        del(gemumu)
    for magician in magicianList:
        del(magician)
    for dragon in dragonList:
        del(dragon)
    


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
    global player, dragonList, lizardList, stage3, portal, dragonCount, lizardCount, gemumuList, magicianList
    
    player.update()
    player.setBackgroundX(stage3.backgroundX)
    
    if( dragonCount > 0 ):
     for dragon in dragonList:
         dragon.update()
         dragon.setBackgroundX(stage3.backgroundX)
         dragon.setPlayerPos(player.x + stage3.backgroundX, player.y)

    
    if( lizardCount > 0 ):
     for lizard in lizardList:
         lizard.setBackgroundX(stage3.backgroundX)
         lizard.setPlayerState( player.state )
         lizard.update()
    if( magicianCount > 0):
        for magician in magicianList:
            magician.setBackgroundX(stage3.backgroundX)
            magician.setPlayerState( player. state)
            magician.update()
    if( gemumuCount > 0):
        for gemumu in gemumuList:
            gemumu.setBackgroundX(stage3.backgroundX)
            gemumu.setPlayerState( player. state)
            gemumu.update()
    portal.setBackgroundX(stage3.backgroundX)
    
    ui.update()

    scroll()
    collision()
    dieCheck()
    stateCheck()



def draw():
    global stage3, player, dragonList, lizardList, portal, dragonCount, lizardCount, gemumuList, magicianList

    clear_canvas()
    stage3.draw()
    
    
    player.draw()
    
    if( lizardCount > 0 ):
     for lizard in lizardList:
          lizard.draw()
    if( gemumuCount > 0 ):
     for gemumu in gemumuList:
          gemumu.draw()
    if( dragonCount > 0 ):
     for dragon in dragonList:
         dragon.draw()
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
    global stage3, player

    if player.state == player.WALK:
        if player.x >= 640:
            if stage3.backgroundX < 340:
                stage3.backgroundX += 5
        elif player.x <= 150:
            if stage3.backgroundX >= 20:
                stage3.backgroundX -= 5

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

    global monsterZenTime, monsterMaxZen, monsterCurZen, dragonList, dragonCount

    
    if time.time() - monsterZenTime >= 8.0:
       if(monsterMaxZen > monsterCurZen):
           monsterZenTime = time.time()
           dragonList.append(dragon())
           dragonCount += 1
           monsterCurZen += 1
# ----------------
def stateCheck():
# ----------------
    global dragonCount, lizardList, dragonList, lizardCount, player, portal, gemumuList, gemumuCount
    global magicianCount, magicianList
    lizardTodragon = 0
    gemumuTodragon = 0
    magicianTodragon = 0
    dragonCheck = 0

    if player.hp <= 0 :
        for dragon in dragonList:
           dragonList.remove(dragon)
        Game_FrameWork.change_state(Title_State)

    if(lizardCount > 0 and dragonCount > 0 ):
        for dragon in dragonList:
            for lizard in lizardList:
                if(lizard.state == lizard.ATTACK and collide(dragon, lizard) == True):
                    lizardTodragon += 1
                 
        for dragon in dragonList:
            for lizard in lizardList:
                if(lizard.state == lizard.ATTACK and collide(dragon, lizard) == False and lizardTodragon == 0):
                    lizard.state = lizard.RUN

    if(magicianCount > 0 and dragonCount > 0 ):
        for dragon in dragonList:
            for magician in magicianList:
                if(magician.state == magician.ATTACK and collide(magician, dragon) == True):
                    magicianTodragon += 1
        for dragon in dragonList:
            for magician in magicianList:
                if(magician.state == magician.ATTACK and collide(magician, dragon) == False and magicianTodragon == 0):
                    magician.state = magician.RUN 

    if(gemumuCount > 0 and dragonCount > 0 ):
        for dragon in dragonList:
            for gemumu in gemumuList:
                if(gemumu.state == gemumu.ATTACK and collide(gemumu, dragon) == True):
                    gemumuTodragon += 1
        for dragon in dragonList:
            for gemumu in gemumuList:
                if(gemumu.state == gemumu.ATTACK and collide(gemumu, dragon) == False and gemumuTodragon == 0):
                    gemumu.state = gemumu.RUN  


    if(gemumuCount > 0 or magicianCount > 0 or lizardCount > 0 and dragonCount > 0):
        for dragon in dragonList:
            for lizard in lizardList:
                if(dragon.state == dragon.ATTACK and collide(lizard, dragon) == True):
                    dragonCheck += 1
        for dragon in dragonList:
            for lizard in lizardList:
                if(dragon.state == dragon.ATTACK and collide(lizard, dragon) == False and dragonCheck == 0 ):
                    dragon.state = dragon.RUN  


        for dragon in dragonList:
            for magician in magicianList:
                if(dragon.state == dragon.ATTACK and collideDefend(magician, dragon) == True):
                    dragonCheck += 1                  
        for dragon in dragonList:
            for magician in magicianList:
                if(dragon.state == dragon.ATTACK and collideDefend(magician, dragon) == False and dragonCheck == 0):
                    dragon.state = dragon.RUN


        for dragon in dragonList:
            for gemumu in gemumuList:
                if(dragon.state == dragon.ATTACK and collideDefend(gemumu, dragon) == True):
                    dragonCheck += 1
        for dragon in dragonList:
            for gemumu in gemumuList:
                if(dragon.state == dragon.ATTACK and collideDefend(gemumu, dragon) == False and dragonCheck == 0):
                    dragon.state = dragon.RUN 

    
# ----------------
def dieCheck():
# ----------------
    global dragonCount, lizardList, dragonList, lizardCount, player, portal, gemumuList, gemumuCount
    global magicianCount, magicianList, ui

    for dragon in dragonList:
        if(dragon.state == dragon.DIE and dragon.frame == dragon.frameNum[dragon.DIE]-1):
                            dragonCount -= 1
                            dragon.frame = 0
                            dragonList.remove(dragon)
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
    global dragonCount, lizardList, dragonList, lizardCount, player, portal, gemumuList, gemumuCount
    global magicianCount, magicianList, ui
    
    if collide(portal, player) and dragonCount == 0:
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

        Game_FrameWork.change_state(Title_State)
        return

    if (lizardCount == 0 and gemumuCount == 0 and magicianCount == 0 ):
        for dragon in dragonList:
            if( dragon.state != dragon.ATTACK and collide(player, dragon) and player.state != player.DIE ):
                dragon.state = dragon.ATTACK
                dragon.frame = 0
            elif( dragon.state == dragon.ATTACK and collide(player, dragon) and dragon.frame == dragon.frameNum[dragon.ATTACK] - 1):
                player.hp -= dragon.att
                dragon.frame = 0
                print(player.hp)
            elif( dragon.state == dragon.ATTACK and True != collide(player, dragon) ):
                dragon.state = dragon.RUN
                dragon.frame = 0

    if( dragonCount == 0):
        for lizard in lizardList:
            lizard.state = lizard.RUN
        for magician in magicianList:
            magician.state = magician.RUN
        for gemumu in gemumuList:
            gemumu.state = gemumu.RUN

    if( dragonCount > 0 and lizardCount > 0):
        for dragon in dragonList:
            for lizard in lizardList:
                if( collide(lizard, dragon) == True ):
                    if(lizard.state == lizard.RUN):
                        lizard.state = lizard.ATTACK
                        lizard.frame = 0
                    elif(lizard.state == lizard.ATTACK):
                        if(lizard.frame == lizard.frameNum[lizard.ATTACK]-1):
                           dragon.hp -= lizard.att
                           lizard.frame = 0
                           print("dragon hp : ", dragon.hp)

                    if(dragon.state == dragon.STAND or dragon.state == dragon.RUN):
                        dragon.state = dragon.ATTACK
                        dragon.frame = 0
                    elif(dragon.state == dragon.ATTACK):
                        if(dragon.frame == dragon.frameNum[dragon.ATTACK]-1):
                            lizard.hp -= dragon.att
                            dragon.frame = 0
                            print("lizard hp : ", lizard.hp)
                    
     
    if( gemumuCount > 0 and dragonCount > 0):
        for dragon in dragonList:
           for gemumu in gemumuList:
                if( collide(gemumu, dragon) == True ):
                    if(gemumu.state == gemumu.RUN):
                        if( gemumu.waveState == 0 ):
                            gemumu.setMonsterX(dragon.x)
                            gemumu.createEnergyWave()
                            gemumu.state = gemumu.ATTACK
                    elif(gemumu.state == gemumu.ATTACK):
                        if( gemumu.waveState == 0 ):
                            gemumu.setMonsterX(dragon.x)
                            gemumu.createEnergyWave()
                        if(gemumu.frame == gemumu.frameNum[gemumu.ATTACK]-1):
                            dragon.hp -= gemumu.att
                            gemumu.frame = 0
                            print("dragon hp : ", dragon.hp)

                if( collideDefend(gemumu, dragon) == True ):
                    if(dragon.state == dragon.STAND or dragon.state == dragon.RUN):
                        dragon.state = dragon.ATTACK
                        dragon.frame = 0
                    elif(dragon.state == dragon.ATTACK):
                        if(dragon.frame == dragon.frameNum[dragon.ATTACK]-1):
                            gemumu.hp -= dragon.att
                            dragon.frame = 0
                            print("gemumu hp : ", gemumu.hp)

    if( magicianCount > 0 and dragonCount > 0):
        for dragon in dragonList:
           for magician in magicianList:
                if( collide(magician, dragon) == True ):
                    if(magician.state == magician.RUN):
                        if( magician.fireState == 0 ):
                            magician.createFire(dragon.x, dragon.y)
                            magician.state = magician.ATTACK
                    elif(magician.state == magician.ATTACK):
                        if( magician.fireState == 0 ):
                            magician.createFire(dragon.x, dragon.y)
                            magician.state = magician.ATTACK
                        if(magician.frame == magician.frameNum[magician.ATTACK]-1):
                            dragon.hp -= magician.att
                            magician.frame = 0
                            print("dragon hp : ", dragon.hp)

                if( collideDefend(magician, dragon) == True ):
                    if(dragon.state == dragon.STAND or dragon.state == dragon.RUN):
                        dragon.state = dragon.ATTACK
                        dragon.frame = 0
                    elif(dragon.state == dragon.ATTACK):
                        if(dragon.frame == dragon.frameNum[dragon.ATTACK]-1):
                            magician.hp -= dragon.att
                            dragon.frame = 0
                            print("magician hp : ", magician.hp)
