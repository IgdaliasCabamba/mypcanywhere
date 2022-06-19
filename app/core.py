from pynput import mouse
from pynput import keyboard
import pprint
import pyautogui
import os
import sys
import requests
import psutil
import platform
import getpass

DISPLAY_MAPPER = 2
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
XDPI = SCREEN_WIDTH // DISPLAY_MAPPER
YDPI = SCREEN_HEIGHT // DISPLAY_MAPPER

keyboard_controller:keyboard.Controller = keyboard.Controller()
mouse_controller:mouse.Controller = mouse.Controller()

if getattr(sys, "frozen", False):
    ROOT_PATH = os.path.dirname(os.path.realpath(sys.executable))
else:
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

routes:dict = {
    "res": os.path.join(ROOT_PATH, "res"),
}

KEYS:dict = {
    "enter":keyboard.Key.enter,
    "esc":keyboard.Key.esc,
    "del":keyboard.Key.backspace,
    "up":keyboard.Key.up,
    "down":keyboard.Key.down,
    "left":keyboard.Key.left,
    "right":keyboard.Key.right,
}

def get_user_name():
    return getpass.getuser()

def get_os():
    return platform.system()

def get_processor():
    return platform.processor()

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    try:
        ip_address = get_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        location_data = {
            "ip": ip_address,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name"),
            "latitude": response.get("latitude"),
            "longitude": response.get("longitude")
        }
        return location_data
    except Exception as e:
        pprint.pprint(e)
        return {
            "ip":"0.0.0.0",
            "city": "Unknow",
            "region": "Unknow",
            "country": "Unknow",
            "latitude": "Unknow",
            "longitude": "Unknow"
        }

def move_mouse(point:tuple):
    try:
        #current_x, current_y = mouse_controller.position
        #x = (point[0]*DISPLAY_MAPPER) - current_x
        #y = (point[1]*DISPLAY_MAPPER) - current_y
        x = (point[0]*DISPLAY_MAPPER)
        y = (point[1]*DISPLAY_MAPPER)
        delta_x:int = int(x*2) 
        delta_y:int = int(y*2)
        #mouse_controller.move(delta_x, delta_y)
        mouse_controller.position = (delta_x, delta_y)

    except Exception as e:
        print(e)

def press_left(obj):
    mouse_controller.press(mouse.Button.left)
    mouse_controller.release(mouse.Button.left)

def press_right(obj):
    mouse_controller.press(mouse.Button.right)
    mouse_controller.release(mouse.Button.right)

def type_key(key:str):
    keyboard_controller.type(key)

def press_key(key_name:str):
    if key_name in KEYS:
        key = KEYS[key_name]
        keyboard_controller.press(key)
        keyboard_controller.release(key)

def get_pc_info():
    return {
            "cpu":psutil.cpu_percent(1),
            "battery":psutil.sensors_battery(),
            "memory":psutil.virtual_memory()
        }