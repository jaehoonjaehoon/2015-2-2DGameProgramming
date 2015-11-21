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
import Title_State



name = "Stage1"

stage1 = None
player = None
font = None

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
    global stage1, player, yetiList, ui, lizard, portal
    stage1 = Stage1()
    player = Player(340)
    lizard = Lizard(player.x)
    ui = UI()
    portal = Portal(1125, 200)

    for i in range(0, 10):
        yetiList.append(Yeti())

def exit():
    global stage1, player, lizard, portal
    del(stage1)
    del(player)
    del(lizard)
    del(portal)



def pause():
    pass


def resume():
    pass


def handle_events():
    global player, UI, lizardMpValue, gemumuMpValue, wizardMpValue, lizardList, lizardButton

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
                 
                               
        else:
           player.handle_events(event)

def update():
    global player, yetiList, lizard, stage1, portal
    
    player.update()
    player.setBackgroundX(stage1.backgroundX)
    
    for yeti in yetiList:
        yeti.update()
        yeti.setBackgroundX(stage1.backgroundX)
        yeti.setPlayerPos(player.x + stage1.backgroundX, player.y)

    #lizard.setBackgroundX(stage1.backgroundX)
    #lizard.setPlayerState( player.state )
    #lizard.setMonsterX( yeti.x )
    #lizard.update()
    
    if( lizardList):
     for lizard in lizardList:
         lizard.setBackgroundX(stage1.backgroundX)
         lizard.setPlayerState( player.state )
         lizard.setMonsterX( yeti.x )
         lizard.update()
    portal.setBackgroundX(stage1.backgroundX)
    
    scroll()
    



def draw():
    global stage1, player, yetiList, lizard, portal

    clear_canvas()
    stage1.draw()
    ui.draw()
    ui.setPlayerHp(player.hp, player.maxHp)
    if( lizardList):
     for lizard in lizardList:
          lizard.draw()
   
     player.draw()
    
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
def collide():
# ----------------
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = a.get_bb()

    if left_a > right_b: return False
    if right_a > left_b: return False
    if top_a > bottom_b: return False
    if bottom_a > top_b: return False

    return True

# ----------------
def collision():
# ----------------
    if collide(door, player):
        Game_FrameWork.change_state(Stage2_State)
        return

    for monster in monsterList:
        if collide(monster, player):
            if player.state == player.SLIDE:
                if monster.state != monster.HIT:
                    monster.soundList[monster.HIT].play()
                    monster.state = monster.HIT
                    monster.frame = 0
                    monster.hp -= player.att

            if player.state == player.WINDMIL:
                if monster.state != monster.HIT and monster.state != monster.DIE:
                    monster.soundList[monster.HIT].play()
                    monster.state = monster.HIT
                    monster.frame = 0
                    monster.hp -= 250

            if player.state == player.KICK:
                if monster.state != monster.HIT and monster.state != monster.DIE:
                    monster.soundList[monster.HIT].play()
                    monster.state = monster.HIT
                    monster.frame = 0
                    monster.hp -= 300

            if player.state == player.NANSA:
                if monster.state != monster.HIT and monster.state != monster.DIE:
                    monster.soundList[monster.HIT].play()
                    monster.state = monster.HIT
                    monster.frame = 0
                    monster.hp -= 600

        for bullet in player.bulletList:
            if collide(bullet, monster):
                if monster.state != monster.HIT and monster.state != monster.DIE:
                    monster.soundList[monster.HIT].play()
                    monster.state = monster.HIT
                    monster.frame = 0
                    monster.hp -= player.att
                    

    for monster in monsterList:
        if monster.state == monster.DIE and monster.frame == monster.frameNum[monster.DIE] - 1:
            monsterList.remove(monster)

        if monster.state != monster.DIE and monster.hp <= 0:
            monster.frame = 0
            monster.state = monster.DIE





