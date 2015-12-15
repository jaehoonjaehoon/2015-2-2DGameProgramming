from pico2d import *

import time
import random

class Mermadia:
   
    mermadiaImage = None

    STAND = 2
    RUN = 2
    ATTACK = 1
    DIE = 0

    # ----------------
    def __init__(self):
    # ----------------
        if Mermadia.mermadiaImage == None:
           Mermadia.mermadiaImage = load_image("Mermadia.png")

        self.frameNum = { self.STAND : 5,
                      self.RUN : 5,
                      self.ATTACK : 7,
                      self.DIE : 3 }

        self.frametime = { self.STAND : 0.1,
                          self.RUN : 0.2,
                          self.ATTACK : 0.5,
                          self.DIE : 0.3 }

        self.state = self.STAND
        self.frame = 0

        self.x, self.y = random.randint(400, 1100), random.randint(150, 300)

        self.currentTime = time.time()
        self.runTime = time.time()
        self.backgroundX = 0
        self.hp = 7000
        self.maxHp = 7000
        self.att = 500

        self.playerX = 0
        self.playerY = 0

        self.mon = 0
        self.startCheck = 0

        self.barNone = load_image("HpBar2.png")
        self.bar = load_image("HpBar.png")
        self.pHp = int(self.hp/self.maxHp) *100


        self.attackSound = load_wav('MermaidaAttack.wav')
        self.attackSound.set_volume(50)

        self.dieSound = load_wav('MermaidaDie.wav')
        self.dieSound.set_volume(50)

        self.soundList = { self.ATTACK : self.attackSound,
                          self.DIE : self.dieSound
            }

    # ----------------
    def update(self):
    # ----------------
        self.frameRate()
        self.move()
        self.motion()
        self.pHp = (self.hp/self.maxHp) * 100
    # ----------------
    def draw(self):
    # ----------------
        self.mermadiaImage.clip_draw(100 * self.frame, (100 * self.state), 
                                        100, 100, self.x - self.backgroundX, self.y)
        #self.draw_bb()
        self.barNone.bar_draw(0, 0, 100, 10, self.x - self.backgroundX- 50, self.y + 300)
        self.bar.bar_draw(0, 0, (int)(100-(100-self.pHp)), 10, self.x - self.backgroundX- 50, self.y + 300)

    # ----------------
    def setBackgroundX(self, x):
    # ----------------
        self.backgroundX = x

    # ----------------
    def setPlayerPos(self, x, y):
    # ----------------
        self.playerX = x
        self.playerY = y

    # ----------------
    def frameRate(self):
    # ----------------
        if time.time() - self.currentTime >= self.frametime[self.state]:
            self.currentTime = time.time()
            self.frame = int(self.frame + 1) % self.frameNum[self.state]
    # ----------------
    def motion(self):
    # ----------------
       if( self.state == self.DIE or self.state == self.ATTACK and self.frame == self.frameNum[self.state]-2):
           self.soundList[self.state].play()
       if( self.hp <= 0):
           self.state = self.DIE
       if time.time() - self.runTime >= 4.0 and self.startCheck == 0:
           self.state = self.RUN
           self.startCheck = 1       

    # ----------------
    def move(self):
    # ----------------
        if self.state == self.RUN and self.x > 10:
            self.x -= 2
        elif self.x <= 10:
            self.x = random.randint(800, 1100)
    # ----------------
    def get_bb(self):
    # ----------------
        return self.x - 50 - self.backgroundX, self.y - 50, self.x + 50 - self.backgroundX, self.y + 50
    # ----------------
    def draw_bb(self):
    # ----------------
        draw_rectangle(*self.get_bb())