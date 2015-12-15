from pico2d import *

class Portal:
    # ----------------
    def __init__(self, x, y):
    # ----------------
        self.x = x
        self.y = y

        self.backgroundX = 0

    # ----------------
    def draw(self):
    # ----------------
       # self.draw_bb()
       pass
    # ----------------
    def setBackgroundX(self, x):
    # ----------------
        self.backgroundX = x

    # ----------------
    def get_bb(self):
    # ----------------
        return self.x - self.backgroundX - 20, self.y + 30, self.x - self.backgroundX + 20, self.y - 70

    # ----------------
    def draw_bb(self):
    # ----------------
        draw_rectangle(*self.get_bb())