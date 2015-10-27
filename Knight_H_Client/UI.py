from pico2d import *

class UI:
    # ----------------
    def __init__(self):
    # ----------------
        self.bar = load_image("UI_Down(800x93).png")
        self.Hp = load_image("HP.png")
        self.Mp = load_image("MP.png")
        self.playerHp = 0
        self.playerMp = 0

    # ----------------
    def update(self):
    # ----------------
        pass
        
    # ----------------
    def draw(self):
    # ----------------
        self.bar.draw(400, 65)
        self.Mp.clip_draw(0, 0 , 80, 80, 760, 65)

    def setPlayerHp(self, hp, maxhp):
        pHp = int(hp/maxhp) * 80 
        self.Hp.clip_draw(0, 0 , 80, (int)(pHp), 40, 65)
        

    