from pico2d import *
import time

class UI:
    # ----------------
    def __init__(self):
    # ----------------
        self.bar = load_image("UI_Down(800x93).png")
        self.Hp = load_image("HP.png")
        self.Mp = load_image("MP.png")
        self.store = load_image("Store.png")
        self.LizardUI = load_image("LizardUI.png")
        self.GemumuUI = load_image("GemumuUI.png")
        self.MagicianUI = load_image("MagicianUI.png")
        self.moneyUI = load_image("MoneyUI.png")
        self.scoreUI = load_image("ScoreUI.png")
        self.boardUI = load_image("BoardUI.png")
        self.playerHp = 0
        self.playerMp = 0
        self.LizardFrame = 0
        self.GemumuFrame = 0
        self.MagicianFrame = 0
        self.storeCheck = False
        self.score = 0
        self.money = 0
        self.font = load_font('ConsolaMalgun.ttf', 20)
        self.time = time.time()

    # ----------------
    def update(self):
    # ----------------
         if time.time() - self.time >= 1.0:
            self.time = time.time()
            self.money += 1

         
        
    # ----------------
    def draw(self):
    # ----------------
        self.bar.draw(400, 65)
        self.LizardUI.clip_draw(self.LizardFrame, 0, 27, 40, 100, 38)
        self.GemumuUI.clip_draw(self.GemumuFrame, 0, 27, 40, 130, 38)
        self.MagicianUI.clip_draw(self.MagicianFrame, 0, 27, 40, 160, 38)
        if(self.storeCheck == True):
            self.store.clip_draw(0, 0, 300, 400, 600, 300)
        self.boardUI.clip_draw(0,0, 250, 100, 100, 550)
        self.moneyUI.clip_draw(0, 0, 38, 38, 20, 580)
        self.scoreUI.clip_draw(0, 0, 38, 38, 20, 530)
        self.font.draw(100, 580, '%d' % (self.money ),(255, 255, 255) )
        self.font.draw(100, 530, '%d' % (self.score ),(255, 255, 255) )
    def drawPlayerHp(self, hp, maxhp):
        pHp = int(hp* 80/maxhp)  
        self.Hp.bar_draw(0, 0 , 80, pHp, 40 - 40, 65 )

    def drawPlayerMp(self, mp, maxmp):
        pMp = int(mp* 80/maxmp)  
        self.Mp.bar_draw(0, 0 , 80, pMp, 760 - 40, 65)
   

    