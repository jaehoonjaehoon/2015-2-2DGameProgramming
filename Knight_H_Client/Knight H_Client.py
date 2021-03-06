﻿import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

import Game_FrameWork
import Logo_State

from pico2d import*

Game_FrameWork.run(Logo_State)

close_canvas()
