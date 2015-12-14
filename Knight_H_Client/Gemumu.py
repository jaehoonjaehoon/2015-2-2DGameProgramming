from pico2d import *

import time
import random
from EnergyWave import EnergyWave

class Gemumu:
   
    GemumuImage = None
    energyWave = None

    RUN = 2
    ATTACK = 1
    DIE = 0

    # ----------------
    def __init__(self, playerX):
    # ----------------
        if Gemumu.GemumuImage == None:
           Gemumu.GemumuImage = load_image("Gemumu.png")

        self.frameNum = {
                      self.RUN : 6,
                      self.ATTACK : 6,
                      self.DIE : 4 }

        self.frametime = { 
                          self.RUN : 0.4,
                          self.ATTACK : 0.2,
                          self.DIE : 0.3 }

        self.state = self.RUN
        self.frame = 0

        
        
        self.x, self.y = playerX + 50 , random.randint(150, 250)

        self.currentTime = time.time()

        self.maxHp = 2500
        self.hp = 2500
        self.att = 100

        self.scrollX = 0
        self.waveState = 0

        self.barNone = load_image("HpBar2.png")
        self.bar = load_image("HpBar.png")
        self.pHp = int(self.hp/self.maxHp) *100


        self.attackSound = load_wav('GemumuAttack.wav')
        self.attackSound.set_volume(64)

        self.dieSound = load_wav('GemumuDie.wav')
        self.dieSound.set_volume(64)

        self.soundList = { self.ATTACK : self.attackSound,
                          self.DIE : self.dieSound
            }
    # ----------------
    def update(self):
    # ----------------
        self.frameRate()
        if self.state != self.DIE:
            self.move()
        self.motion()
        self.pHp = (self.hp/self.maxHp) * 100

    # ----------------
    def draw(self):
    # ----------------
        self.GemumuImage.clip_draw(100 * self.frame, (100 * self.state), 
                                    100, 100, self.x - self.backgroundX, self.y)
        self.draw_bb()
        if(self.waveState == 1):
            self.energyWave.setBackgroundX(self.backgroundX)
            self.energyWave.draw()
        self.barNone.bar_draw(0, 0, 100, 10, self.x - self.backgroundX- 50, self.y + 300)
        self.bar.bar_draw(0, 0, (int)(100-(100-self.pHp)), 10, self.x - self.backgroundX- 50, self.y + 300)

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
            if(self.waveState == 1 and self.state == self.ATTACK ):
                 self.energyWave.update()
                 if(self.energyWave.frame == (self.energyWave.frameNum - 1)):
                     del(self.energyWave)
                     self.waveState = 0
            if(self.waveState == 1 and self.state == self.RUN ):
                     del(self.energyWave)
                     self.waveState = 0        
      
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
    def get_bb_defend(self):
    # ----------------
        return self.x - 50 - self.backgroundX, self.y - 50, self.x + 50 - self.backgroundX, self.y + 50
    # ----------------
    # ----------------
    def get_bb(self):
    # ----------------
        return self.x - 100 - self.backgroundX, self.y - 100, self.x + 300 - self.backgroundX, self.y + 100
    # ----------------
    def draw_bb(self):
    # ----------------
        draw_rectangle(*self.get_bb())


    # ----------------충돌시 생성
    def createEnergyWave(self):
    #-----------------
        self.energyWave = EnergyWave(self.x+90, self.y, self.monsterX, self.backgroundX)
        self.waveState = 1
    
    