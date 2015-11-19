from pico2d import *

import time
import random

class Yeti:
   
    yetiImage = None

    STAND = 4
    RUN = 3
    ATTACK = 2
    HIT = 1
    DIE = 0

    # ----------------
    def __init__(self):
    # ----------------
        if Yeti.yetiImage == None:
           Yeti.yetiImage = load_image("Yeti.png")

        self.frameNum = { self.STAND : 3,
                      self.RUN : 4,
                      self.ATTACK : 4,
                      self.HIT : 2,
                      self.DIE : 4 }

        self.frametime = { self.STAND : 0.1,
                          self.RUN : 0.2,
                          self.ATTACK : 0.05,
                          self.HIT : 0.3,
                          self.DIE : 0.3 }

        self.state = self.RUN
        self.frame = 0

        self.x, self.y = random.randint(400, 1100), random.randint(150, 300)

        self.currentTime = time.time()

        self.hp = 1200
        self.att = 150

        self.playerX = 0
        self.playerY = 0

        self.mon = 0
        self.maxHp = 1200

    # ----------------
    def update(self):
    # ----------------
        self.frameRate()
        #if self.state != self.DIE:
            #self.moveToPlayer()
        self.move()

    # ----------------
    def draw(self):
    # ----------------
        self.yetiImage.clip_draw(150 * self.frame, (150 * self.state), 
                                        150, 150, self.x - self.backgroundX, self.y)
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

        if self.state != self.DIE:
            if self.frame == self.frameNum[self.state] - 1:
                self.state = self.STAND
                self.frame = 0

    # ----------------
    def move(self):
    # ----------------
        if self.state != self.ATTACK and self.x > 10:
            self.x -= 5
    # ----------------
    def get_bb(self):
    # ----------------
        return self.x - 50 + self.backgroundX, self.y - 50, self.x + 50 + self.backgroundX, self.y + 50
    # ----------------
    def draw_bb(self):
    # ----------------
        draw_rectangle(*self.get_bb())