# coding: utf-8

import os

if "win32" in os.sys.platform:
    SCREEN_SHOOT_SAVE_PATH = os.path.join(os.getcwd(), 'screen_shoot')
    STORAGE_PATH = os.path.join(os.getcwd() + "storage")
else:
    SCREEN_SHOOT_SAVE_PATH = os.path.join(os.getcwd() + 'screen_shoot')
    STORAGE_PATH = os.path.join(os.getcwd() + 'storage')
