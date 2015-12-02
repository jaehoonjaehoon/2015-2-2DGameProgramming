import Game_FrameWork
import Title_State
from pico2d import *


name = "LogoState"
image = None
logo_time = 0.0
logoBgm = None


def enter():
    global image, logoBgm
    open_canvas()
    image = load_image('Logo_State.png')

    logoBgm = load_music('logoBgm.mp3')
    logoBgm.set_volume(64)
    logoBgm.repeat_play()



def exit():
   global image, logoBgm
   del(image)
   del(logoBgm)
   close_canvas()

def update():
    global logo_time

    if( logo_time > 1.0):
        logo_time = 0
        Game_FrameWork.push_state(Title_State)
    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




