from pico2d import *

energyWaveImage = None

class EnergyWave:
    # ----------------
    def __init__(self, x, y):
    # ----------------
        global energyWaveImage


        if energyWaveImage == None:
            energyWaveImage = load_image("EnergyWave.png")


        self.x = x
        self.y = y

    # ----------------
    def update(self):
    # ----------------
        self.x += 50


    # ----------------
    def draw(self):
    # ----------------
        self.energyWaveImage.clip_draw(0, 70, 40, 70, self.x, self.y)


    # ----------------
    def get_bb(self):
    # ----------------
        return self.x - 25, self.y + 15, self.x + 25, self.y - 15

    # ----------------
    def draw_bb(self):
    # ----------------
        draw_rectangle(*self.get_bb())