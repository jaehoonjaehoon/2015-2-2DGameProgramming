from pico2d import *

import time
import random
from Fire import Fire

class Magician:
   
    MagicianImage = None
    fire = None
    
    RUN = 2
    ATTACK = 1
    DIE = 0

    # ----------------
    def __init__(self, playerX):
    # ----------------
        if Magician.MagicianImage == None:
           Magician.MagicianImage = load_image("Magician.png")

        self.frameNum = { 
                      self.RUN : 4,
                      self.ATTACK : 5,
                      self.DIE : 3 }

        self.frametime = { 
                          self.RUN : 0.4,
                          self.ATTACK : 0.5,
                          self.DIE : 0.3 }

        self.state = self.RUN
        self.frame = 0

        self.x, self.y = playerX + 50 , random.randint(150, 250)

        self.currentTime = time.time()
        self.attackSound = load_wav('MagicianAttack.wav')
        self.attackSound.set_volume(64)

        self.dieSound = load_wav('MagicianDie.wav')
        self.dieSound.set_volume(64)

        self.soundList = { self.ATTACK : self.attackSound,
                          self.DIE : self.dieSound
                          }
        self.maxHp = 1500
        self.hp = 1500
        self.att = 250

        self.monsterX = 0
        self.monsterY = 0
        self.scrollX = 0
        self.fireState = 0
    # ----------------
    def update(self):
    # ----------------
        self.frameRate()
        if self.state != self.DIE:
            self.move()
        self.motion()
        

    # ----------------
    def draw(self):
    # ----------------
        self.MagicianImage.clip_draw(100 * self.frame, (100 * self.state), 
                                    100, 100, self.x - self.backgroundX, self.y)
        self.draw_bb()
        if(self.fireState == 1):
            self.fire.setBackgroundX(self.backgroundX)
            self.fire.draw()
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
            if(self.fireState == 1 and self.state == self.ATTACK ):
                 self.fire.update()
                 if(self.fire.frame == (self.fire.frameNum - 1)):
                     del(self.fire)
                     self.fireState = 0
            if(self.fireState == 1 and self.state == self.RUN ):
                   del(self.fire)
                   self.fireState = 0 
     
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
    # ----------------
    def get_bb_defend(self):
    # ----------------
        return self.x - 50 - self.backgroundX, self.y - 50, self.x + 50 - self.backgroundX, self.y + 50
    # ----------------
    def get_bb(self):
    # ----------------
        return self.x - 50 - self.backgroundX, self.y - 50, self.x + 150 - self.backgroundX, self.y + 50
    # ----------------
    def draw_bb(self):
    # ----------------
        draw_rectangle(*self.get_bb())
    # ----------------충돌시 생성
    def createFire(self, mX, mY):
    #-----------------
        self.fire = Fire(mX, mY, self.backgroundX)
        self.fireState = 1
    