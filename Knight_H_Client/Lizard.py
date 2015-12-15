from pico2d import *

import time
import random

class Lizard:
   
    LizardImage = None
    barNone = None
    bar = None
    STAND = 3
    RUN = 2
    ATTACK = 1
    DIE = 0

    # ----------------
    def __init__(self, playerX):
    # ----------------
        if Lizard.LizardImage == None:
           Lizard.LizardImage = load_image("Lizard.png")

        self.frameNum = { self.STAND : 4,
                      self.RUN : 4,
                      self.ATTACK : 5,
                      self.DIE : 3 }

        self.frametime = { self.STAND : 0.1,
                          self.RUN : 0.4,
                          self.ATTACK : 0.3,
                          self.DIE : 0.5 }
        self.attackSound = load_wav('LizardAttack.wav')
        self.attackSound.set_volume(64)

        

        self.dieSound = load_wav('LizardDie.wav')
        self.dieSound.set_volume(64)

        self.soundList = { self.ATTACK : self.attackSound,
                          self.DIE : self.dieSound
            }

        self.state = self.RUN
        self.frame = 0

        self.x, self.y = playerX + 50 , random.randint(150, 250)

        self.currentTime = time.time()
        self.attackTime = 0.0

        self.maxHp = 2000
        self.hp = 2000
        
        self.barNone = load_image("HpBar2.png")
        self.bar = load_image("HpBar.png")
        self.pHp = int(self.hp/self.maxHp) *100

        self.att = 50

        self.monsterX = 0
        self.monsterY = 0
        self.scrollX = 0

    # ----------------
    def update(self):
    # ----------------
        self.frameRate()
        if self.state != self.STAND:
            self.move()
        self.motion()
        self.pHp = (self.hp/self.maxHp) * 100
    # ----------------
    def draw(self):
    # ----------------
        self.LizardImage.clip_draw(100 * self.frame, (100 * self.state), 
                                    100, 100, self.x - self.backgroundX, self.y)
        self.barNone.bar_draw(0, 0, 100, 10, self.x - self.backgroundX- 50, self.y + 300)
        self.bar.bar_draw(0, 0, (int)(100-(100-self.pHp)), 10, self.x - self.backgroundX- 50, self.y + 300)

       # self.draw_bb()
    # ----------------
    def setPlayerState(self, state):
    # ----------------
        
        if state == 2:
            self.state = self.DIE
    # ----------------
    def setBackgroundX(self, x):
    # ----------------
        self.backgroundX = x
    # ----------------
    def setMonsterX(self, x):
    # ----------------
        self.monsterX = x

    # ----------------
    def frameRate(self):
    # ----------------
        if time.time() - self.currentTime >= self.frametime[self.state]:
            self.currentTime = time.time()
            self.frame = int(self.frame + 1) % self.frameNum[self.state]

        
      
    # ----------------
    def move(self):
    # ----------------
       if self.x < 1125 and self.state == self.RUN :
          self.x += 2 
       

    # ----------------
    def motion(self):
    # ----------------
       if( self.state != self.RUN and self.frame == self.frameNum[self.state]-2):
           self.soundList[self.state].play()

       if( self.hp <= 0):
           self.state = self.DIE
       
    # ----------------
    def get_bb(self):
    # ----------------
        return self.x - 50 - self.backgroundX, self.y - 50, self.x + 50 - self.backgroundX, self.y + 50
    # ----------------
    def draw_bb(self):
    # ----------------
        draw_rectangle(*self.get_bb())