# this ensures our pixel coordinates will not be modified
import ctypes
PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)

from Captchat import is_captchat

from pynput import mouse, keyboard
from pynput.mouse import Button, Controller as ControllerM
from pynput.keyboard import Key, Controller as ControllerK
import time
import pyautogui
from PIL import Image

# MODE D'EMPLOI
# ------------
# Avoir que des havres-gemmes jardin
# Avoir un écran de 1920 x 1080
# Dézoomer au max
# Placer son perso tout en haut de la grille
# Retirer tous ses équipements, ou laisser son chapeau si les cheveux sont rouges
# Avoir des pousses au raccourcis 8 (testé avec topinambour uniquement pour l'instant)
# --------------

# --- CONFIG ---

log = False

mouseInput = ControllerM()
keyInput = ControllerK()
print("Startup")
startupTime = 5
print("The program will start in " + str(startupTime) + " seconds")
time.sleep(startupTime)

def on_click(x, y, button, pressed):
    if pressed and log:
        print(str(button) + " click at " + str(x) + " " + str(y))

def on_press(key):
    if log:
        try:
            print('alphanumeric key {0} pressed'.format(key.char))
        except AttributeError:
            print('special key {0} pressed'.format(key))

listenerM = mouse.Listener(on_click=on_click)
listenerM.start()
listenerK = keyboard.Listener(on_press=on_press)
listenerK.start()

# -----------------

# Utilities -------

# plants coords ---

tree_base_x = 900
tree_base_y = 520

plant_base_x = 905
plant_base_y = 580

harvest_plant_seeds_x = 825
harvest_plant_seeds_y = 485

harvest_plant_x = 855
harvest_plant_y = 515

# ------------------

# X X X
# X O X
# X X X
wak_center_x = 960
wak_center_y = 550

# X X X
# X X X
# O X X
wak_leftdown_x = 905
wak_leftdown_y = 575

# X X X
# O X X
# X X X
wak_left_x = 845
wak_left_y = 545

# O X X
# X X X
# X X X
wak_leftup_x = 905
wak_leftup_y = 520

# X O X
# X X X
# X X X
wak_up_x = 965
wak_up_y = 490

# X X O
# X X X
# X X X
wak_rightup_x = 1020
wak_rightup_y = 520

# X X X
# X X O
# X X X
wak_right_x = 1080
wak_right_y = 545

# X X X
# X X X
# X X O
wak_rightdown_x = 1020
wak_rightdown_y = 575

# X X X
# X X X
# X O X
wak_down_x = 965
wak_down_y = 605

def click_at(x, y):
    mouseInput.position = (x, y)
    mouseInput.click(Button.left, 1)

def right_click_center():
    mouseInput.position = (wak_center_x, wak_center_y)
    mouseInput.click(Button.right, 1)

def right_click_leftdown():
    mouseInput.position = (wak_leftdown_x, wak_leftdown_y)
    mouseInput.click(Button.right, 1)

def click_center():
    mouseInput.position = (wak_center_x, wak_center_y)
    mouseInput.click(Button.left, 1)

def click_leftdown():
    mouseInput.position = (wak_leftdown_x, wak_leftdown_y)
    mouseInput.click(Button.left, 1)

def click_left():
    mouseInput.position = (wak_left_x, wak_left_y)
    mouseInput.click(Button.left, 1)

def click_leftup():
    mouseInput.position = (wak_leftup_x, wak_leftup_y)
    mouseInput.click(Button.left, 1)

def click_up():
    mouseInput.position = (wak_up_x, wak_up_y)
    mouseInput.click(Button.left, 1)

def click_rightup():
    mouseInput.position = (wak_rightup_x, wak_rightup_y)
    mouseInput.click(Button.left, 1)

def click_right():
    mouseInput.position = (wak_right_x, wak_right_y)
    mouseInput.click(Button.left, 1)

def click_rightdown():
    mouseInput.position = (wak_rightdown_x, wak_rightdown_y)
    mouseInput.click(Button.left, 1)

def click_down():
    mouseInput.position = (wak_down_x, wak_down_y)
    mouseInput.click(Button.left, 1)

# Screen -------------

def is_tree_planted():
    screenshot = pyautogui.screenshot()
    (r, g, b) = screenshot.getpixel((tree_base_x, tree_base_y))
    if r > g:
        return True
    print("red: " + str(r) + ", green: " + str(g))
    return False

def is_plant_planted():
    screenshot = pyautogui.screenshot()
    (r, g, b1) = screenshot.getpixel((plant_base_x, plant_base_y))
    (r, g, b2) = screenshot.getpixel((plant_base_x + 3, plant_base_y))
    (r, g, b3) = screenshot.getpixel((plant_base_x - 3, plant_base_y))
    (r, g, b4) = screenshot.getpixel((plant_base_x + 6, plant_base_y))
    (r, g, b5) = screenshot.getpixel((plant_base_x - 6, plant_base_y))
    (r, g, b6) = screenshot.getpixel((plant_base_x, plant_base_y - 5))
    (r, g, b7) = screenshot.getpixel((plant_base_x + 3, plant_base_y - 5))
    (r, g, b8) = screenshot.getpixel((plant_base_x - 3, plant_base_y - 5))
    (r, g, b9) = screenshot.getpixel((plant_base_x + 6, plant_base_y - 5))
    (r, g, b10) = screenshot.getpixel((plant_base_x - 6, plant_base_y - 5))
    if b1 > 4 or b2 > 4 or b3 > 4 or b4 > 4 or b5 > 4 or b6 > 4 or b7 > 4 or b8 > 4 or b9 > 4 or b10 > 4:
        return True
    print("not enough blue")
    return False

# Keys ---------------

def press_8():
    keyInput.press('_')
    keyInput.release('_')

# --------------------

# Main code ----------

# Common -------------

def back_to_initial():
    i = 0
    while i <= 17:
        click_rightup()
        time.sleep(0.4)
        i += 1
    i = 0
    while i <= 17:
        click_leftup()
        time.sleep(0.4)
        i += 1

# Trees --------------

def plant_leftup_tree():
    rerun = False
    while(True):
        if not rerun:
            press_8()
            time.sleep(0.05)
            click_left()
            time.sleep(0.05)
            right_click_center()
            time.sleep(4.5)
            if is_tree_planted():
                break
            else:
                rerun = True
        else:
            press_8()
            click_leftup()
            right_click_center()
            time.sleep(4.5)
            if is_tree_planted():
                break

def plant_up_tree():
    while(True):
        press_8()
        click_leftup()
        right_click_center()
        time.sleep(4.5)
        if is_tree_planted():
            break

def plant_line_trees():
    i = 0
    while (i < 17):
        if i == 0:
            plant_up_tree()
        else:
            plant_leftup_tree()
        i += 1

def plant_grid_trees():
    i = 0
    while (i < 8):
        plant_line_trees()
        j = 0
        click_rightdown()
        time.sleep(0.4)
        click_rightdown()
        time.sleep(0.4)
        while (j < 16):
            click_rightup()
            time.sleep(0.4)
            j += 1
        i += 1

# -------------------------------

# Plants --------------

def plant_leftdown_plant():
    while(True):
        press_8()
        time.sleep(0.05)
        click_leftdown()
        time.sleep(0.05)
        right_click_center()
        time.sleep(4.5)
        if is_plant_planted():
            break

def plant_line_plants():
    i = 0
    while (i < 17):
        plant_leftdown_plant()
        click_leftdown()
        time.sleep(0.4)
        i += 1

def plant_grid_plants():
    i = 0
    while (i < 17):
        plant_line_plants()
        j = 0
        click_rightdown()
        time.sleep(0.4)
        while (j < 17):
            click_rightup()
            time.sleep(0.4)
            j += 1
        i += 1

def harvest_leftdown_plant():
    time.sleep(0.05)
    right_click_leftdown()
    time.sleep(0.2)
    screen = pyautogui.screenshot()
    (r, g, b) = screen.getpixel((harvest_plant_seeds_x, harvest_plant_seeds_y))
    if r == 255:
        click_at(harvest_plant_seeds_x, harvest_plant_seeds_y)
        is_captchat()

    time.sleep(0.05)
    right_click_leftdown()
    time.sleep(0.2)
    click_at(harvest_plant_x, harvest_plant_y)
    is_captchat()
    

def harvest_line_plants():
    i = 0
    while (i < 17):
        harvest_leftdown_plant()
        click_leftdown()
        time.sleep(0.4)
        i += 1

def harvest_grid_plants():
    i = 0
    while (i < 17):
        harvest_line_plants()
        j = 0
        click_rightdown()
        time.sleep(0.4)
        while (j < 17):
            click_rightup()
            time.sleep(0.4)
            j += 1
        i += 1

# ------------------------------

plant_grid_plants()
back_to_initial()
harvest_grid_plants()
