﻿from pico2d import *

import time
import random

class Lizard:
   
    LizardJImage = None

    STAND = 3
    RUN = 2
    ATTACK = 1
    DIE = 0

    # ----------------
    def __init__(self, playerX):
    # ----------------
        if Lizard.LizardJImage == None:
           Lizard.LizardJImage = load_image("KnightJ.png")

        self.frameNum = { self.STAND : 4,
                      self.RUN : 4,
                      self.ATTACK : 5,
                      self.DIE : 3 }

        self.frametime = { self.STAND : 0.1,
                          self.RUN : 0.4,
                          self.ATTACK : 0.05,
                          self.DIE : 0.3 }

        self.state = self.RUN
        self.frame = 0

        self.x, self.y = playerX + 50 , random.randint(150, 250)

        self.currentTime = time.time()

        self.maxHp = 1500
        self.hp = 1500
        self.att = 200

        self.monsterX = 0
        self.monsterY = 0
        self.playerDir = 1

    # ----------------
    def update(self):
    # ----------------
        self.frameRate()
        if self.state != self.STAND:
            self.move()

    # ----------------
    def draw(self):
    # ----------------
        self.LizardJImage.clip_draw(100 * self.frame, (100 * self.state), 
                                    100, 100, self.x - self.backgroundX, self.y)
    # ----------------
    def setPlayerState(self, state):
    # ----------------
        if state == 0:
            self.state = self.STAND
        elif state == 1:
            self.state = self.RUN
    # ----------------
    def setPlayerDir(self, dir):
    # ----------------
        self.playerDir = dir

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

        if self.state != self.DIE:
            if self.frame == self.frameNum[self.state] - 1:
                self.state = self.STAND
                self.frame = 0
      
    # ----------------
    def move(self):
    # ----------------
       if self.x < 800 and self.state == self.RUN and self.playerDir == 1:
          self.x += 5 
       elif self.x < 800 and self.state == self.RUN and self.playerDir == 2:
          self.x -= 5 