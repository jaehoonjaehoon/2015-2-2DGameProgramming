import Game_FrameWork
import Stage1_State
import Stage2_State
import Stage3_State

from pico2d import *
from pico2d import load_music

name = "TitleState"
image = None
titleBgm = None

def enter():
    global image, titleBgm
    image = load_image('Title_State.png')
    
    titleBgm = load_music('TitleBgm.mp3')
    titleBgm.set_volume(64)
    titleBgm.repeat_play()



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_FrameWork.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_FrameWork.quit()
            elif ( event.type, event.key ) == (SDL_KEYDOWN, SDLK_SPACE):
                Game_FrameWork.change_state(Stage3_State)

# ----------------
def draw():
# ----------------

    clear_canvas()
    image.draw(400,300)
    update_canvas()

# ----------------
def exit():
# ----------------
    global image, titleBgm

    del(image)
    del(titleBgm)





def update():
    pass


def pause():
    pass


def resume():
    pass
