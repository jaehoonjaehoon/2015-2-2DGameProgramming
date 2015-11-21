from pico2d import *

import time

class Player:
    playerImage = None
    
    UP_DIR = 0
    RIGHT_DIR = 1
    LEFT_DIR = 2
    DOWN_DIR = 3

    STAND = 0
    WALK = 1
    DIE = 2


    #-----------------
    def __init__(self, scroll):
    #-----------------
        self.x = 150
        self.y = 150

        self.maxHp = 1000
        self.hp = 1000
        self.maxMp = 200
        self.mp = 200

        self.scroll = scroll
        
        self.frame = 0
        self.playerImage = load_image("Player.png")
        self.dir = self.DOWN_DIR
        self.frametime = { self.STAND : 0.1,
                          self.WALK : 0.2}
        self.frameNum = { self.STAND : 4,
                      self.WALK : 4}
        self.state = self.STAND

        self.moveSpeed = 5
        self.currentTime = time.time()
        self.backgroundX = 0

        self.inputUpKey = False
        self.inputDownKey = False
        self.inputLeftKey = False
        self.inputRightKey = False

    #-----------------
    def update(self):
    #-----------------
        self.move()
        self.frameRate()

    #-----------------
    def draw(self):
    #-----------------
        self.playerImage.clip_draw(self.frame * 150, self.dir * 150 , 150, 150, self.x, self.y)

    # ----------------
    def handle_events(self, event):
    # ----------------
        # SDL_KEYDOWN

        if event.type == SDL_KEYDOWN:

            if event.key == SDLK_RIGHT:
                self.dir = self.RIGHT_DIR
                self.inputRightKey = True

                self.state = self.WALK
                self.frame = 0
  
            elif event.key == SDLK_LEFT:
                self.dir = self.LEFT_DIR
                self.inputLeftKey = True

                self.state = self.WALK
                self.frame = 0

            elif event.key == SDLK_UP:
                self.dir = self.UP_DIR
                self.inputUpKey = True

                self.state = self.WALK
                self.frame = 0

            elif event.key == SDLK_DOWN:
                self.dir = self.DOWN_DIR
                self.inputDownKey = True

                self.state = self.WALK
                self.frame = 0

        # SDL_KEYUP
        elif event.type == SDL_KEYUP:

            if event.key == SDLK_RIGHT:
                self.inputRightKey = False

                self.state = self.STAND
                self.frame = 0
            
            elif event.key == SDLK_LEFT:
                self.inputLeftKey = False

                self.state = self.STAND
                self.frame = 0

            elif event.key == SDLK_UP:
                self.inputUpKey = False

                self.state = self.STAND
                self.frame = 0
                
            elif event.key == SDLK_DOWN:
                self.inputDownKey = False

                self.state = self.STAND
                self.frame = 0

           
    # ----------------
    def move(self):
    # ----------------
        if self.state == self.WALK:
            if self.dir == self.RIGHT_DIR:
                if self.inputRightKey == True:
                    if self.backgroundX >= self.scroll:
                        if self.x < 785:
                            self.x += self.moveSpeed

                    else:
                        if self.x < 645:
                            self.x += self.moveSpeed

            elif self.dir == self.LEFT_DIR:
                if self.inputLeftKey == True:
                    if self.backgroundX <= 0:
                        if self.x > 15:
                            self.x -= self.moveSpeed
                    else:
                        if self.x > 150:
                            self.x -= self.moveSpeed
            elif self.dir == self.UP_DIR:
                if self.inputUpKey == True:
                    if self.y < 250:
                       self.y += self.moveSpeed
            elif self.dir == self.DOWN_DIR:
                if self.inputDownKey == True:
                    if self.y > 170:
                       self.y -= self.moveSpeed
  
    # ----------------
    def frameRate(self):
    # ----------------
        if time.time() - self.currentTime >= self.frametime[self.state]:
            self.currentTime = time.time()
            self.frame = int(self.frame + 1) % self.frameNum[self.state]

        if self.frame == self.frameNum[self.state]:
            self.frame = 0
            self.state = self.STAND

    # ----------------
    def setBackgroundX(self, x):
    # ----------------
        self.backgroundX = x
