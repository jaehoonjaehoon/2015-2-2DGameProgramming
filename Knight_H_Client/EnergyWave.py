from pico2d import *
import time



class EnergyWave:
    
    energyWaveImage = None

    # ----------------
    def __init__(self, x, y, mX, bX):
    # ----------------


        if self.energyWaveImage == None:
            self.energyWaveImage = load_image("EnergyWave.png")


        self.x = x
        self.y = y
        self.frame = 0
        self.currentTime = time.time()
        self.backgroundX = bX
        self.frametime = 0.5
        self.frameNum = 4
        self.monsterX = mX
        self.distance = int((self.monsterX - self.x)/self.frameNum)

    # ----------------
    def update(self):
    # ----------------
        self.frameRate()
        self.move()
        
    # ----------------
    def draw(self):
    # ----------------
        self.energyWaveImage.clip_draw(70 * self.frame, 0, 70, 70, self.x - self.backgroundX, self.y)
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
        print(self.currentTime)
        print(time.time())
        if time.time() - self.currentTime >= self.frametime:
            self.currentTime = time.time()
            self.frame = int(self.frame + 1) % self.frameNum
    # ----------------
    def setBackgroundX(self, x):
    # ----------------
        self.backgroundX = x
    
    # ----------------
    def setMonsterX(self, x):
    # ----------------
        self.monsterX = x
    # ----------------
    def move(self):
    # ----------------
        if(self.x <= self.monsterX):
                self.x += self.distance
    