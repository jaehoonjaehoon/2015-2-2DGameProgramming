from pico2d import *

import time
import random

class Magician:
   
    MagicianImage = None

    
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

        self.maxHp = 2500
        self.hp = 2500
        self.att = 50

        self.monsterX = 0
        self.monsterY = 0
        self.scrollX = 0

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
       pass
    # ----------------
    def get_bb(self):
    # ----------------
        return self.x - 50 - self.backgroundX, self.y - 50, self.x + 50 - self.backgroundX, self.y + 50
    # ----------------
    def draw_bb(self):
    # ----------------
        draw_rectangle(*self.get_bb())