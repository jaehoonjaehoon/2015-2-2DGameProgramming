from pico2d import *
import time



class Fire:
    
    fireImage = None

    # ----------------
    def __init__(self, mX, mY, bX):
    # ----------------


        if self.fireImage == None:
            self.fireImage = load_image("Fire.png")


        self.x = mX
        self.y = mY
        self.frame = 0
        self.currentTime = time.time()
        self.backgroundX = bX
        self.frametime = 0.75
        self.frameNum = 4
        self.monsterX = mX
        self.monsterY = mY

    # ----------------
    def update(self):
    # ----------------
        self.frameRate()
        
    # ----------------
    def draw(self):
    # ----------------
        self.fireImage.clip_draw(100 * self.frame, 0, 200, 140, self.x - self.backgroundX, self.y)
    # ----------------
    def get_bb(self):
    # ----------------
        return self.x - 25, self.y + 15, self.x + 25, self.y - 15

    # ----------------
    def draw_bb(self):
    # ----------------
        draw_rectangle(*self.get_bb())

    # ----------------
    def frameRate(self):
    # ----------------
        if time.time() - self.currentTime >= self.frametime:
            self.currentTime = time.time()
            self.frame = int(self.frame + 1) % self.frameNum
    # ----------------
    def setBackgroundX(self, x):
    # ----------------
        self.backgroundX = x
    
    # ----------------
    def setMonsterX(self, x, y):
    # ----------------
        self.monsterX = x
        self.monsterY = x
    
    