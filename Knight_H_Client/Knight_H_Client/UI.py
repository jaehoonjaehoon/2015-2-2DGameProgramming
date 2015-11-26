from pico2d import *

class UI:
    # ----------------
    def __init__(self):
    # ----------------
        self.bar = load_image("UI_Down(800x93).png")
        self.Hp = load_image("HP.png")
        self.Mp = load_image("MP.png")
        self.LizardUI = load_image("LizardUI.png")
        self.GemumuUI = load_image("GemumuUI.png")
        self.WizardUI = load_image("WizardUI.png")
        self.playerHp = 0
        self.playerMp = 0
        self.LizardFrame = 0
        self.GemumuFrame = 0
        self.WizardFrame = 0

    # ----------------
    def update(self):
    # ----------------
        pass
        
    # ----------------
    def draw(self):
    # ----------------
        self.bar.draw(400, 65)
        self.Mp.clip_draw(0, 0 , 80, 80, 760, 65)
        self.LizardUI.clip_draw(self.LizardFrame, 0, 27, 40, 100, 38)
        self.GemumuUI.clip_draw(self.GemumuFrame, 0, 27, 40, 130, 38)
        self.WizardUI.clip_draw(self.WizardFrame, 0, 27, 40, 160, 38)

    def setPlayerHp(self, hp, maxhp):
        pHp = int(hp/maxhp) * 80 
        self.Hp.clip_draw(0, 0 , 80, pHp, 40, 65)
        

    