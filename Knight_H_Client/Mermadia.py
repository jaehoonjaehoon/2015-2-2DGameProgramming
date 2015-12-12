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
        self.backgroundX = 0
        self.hp = 7000
        self.att = 500

        self.playerX = 0
        self.playerY = 0

        self.mon = 0
        self.maxHp = 1200

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

    # ----------------
    def draw(self):
    # ----------------
        self.mermadiaImage.clip_draw(100 * self.frame, (100 * self.state), 
                                        100, 100, self.x - self.backgroundX, self.y)
        self.draw_bb()

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
       if( self.state == self.DIE or self.state == self.ATTACK and self.frame == self.frameNum[self.state]-1):
           self.soundList[self.state].play()
        

    # ----------------
    def move(self):
    # ----------------
        if self.state == self.RUN and self.x > 10:
            self.x -= 2
    # ----------------
    def get_bb(self):
    # ----------------
        return self.x - 50 - self.backgroundX, self.y - 50, self.x + 50 - self.backgroundX, self.y + 50
    # ----------------
    def draw_bb(self):
    # ----------------
        draw_rectangle(*self.get_bb())