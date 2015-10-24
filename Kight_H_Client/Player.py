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


    #-----------------
    def __init__(self):
    #-----------------
        self.x = 150
        self.y = 150
        self.frame = 0
        self.playerImage = load_image("Player.png")
        self.dir = self.DOWN_DIR
        self.frametime = { self.STAND : 0.1,
                          self.WALK : 0.05}
        self.frameNum = { self.STAND : 4,
                      self.WALK : 4}
        self.state = self.STAND

        self.moveSpeed = 5

        self.inputUpKey = False
        self.inputDownKey = False
        self.inputLeftKey = False
        self.inputRightKey = False

    #-----------------
    def update(self):
    #-----------------
        self.frame += (self.frame+1)% self.frameNum[self.state]
        self.move()

    #-----------------
    def draw(self):
    #-----------------
        self.playerImage.clip_draw(self.frame * 100, self.dir * 100 , 100, 100, self.x, self.y)

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
            if self.dir == self.UP_DIR:
                if self.inputUpKey == True:
                    if self.y <= 300:
                        self.y += self.moveSpeed
            elif self.dir == self.DOWN_DIR:
                if self.inputDownKey == True:
                     if self.y >= 00:
                        self.y -= self.moveSpeed
            elif self.dir == self.RIGHT_DIR:
                if self.inputRightKey == True:
                      if self.x < 785:
                         self.x += self.moveSpeed
            elif self.dir == self.LEFT_DIR:
                if self.inputLeftKey == True:
                    if self.x > 0:
                        self.x -= self.moveSpeed

 
