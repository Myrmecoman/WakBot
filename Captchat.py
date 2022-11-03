# this ensures our pixel coordinates will not be modified
import ctypes
PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)

from pynput import mouse, keyboard
from pynput.mouse import Button, Controller as ControllerM
from pynput.keyboard import Key, Controller as ControllerK
import time
import pyautogui
from PIL import Image

# Inputs ----------------------------------

mouseInput = ControllerM()
keyInput = ControllerK()

wak_center_x = 960
wak_center_y = 550

close_x = 1420
close_y = 472

def click_at(x, y):
    mouseInput.position = (x, y)
    mouseInput.click(Button.left, 1)

def three_captchat_clicks_at(x, y):
    press_1()
    time.sleep(0.3)
    mouseInput.position = (x, y)
    mouseInput.click(Button.left, 1)
    time.sleep(0.3)
    press_1()
    time.sleep(0.3)
    mouseInput.position = (x, y)
    mouseInput.click(Button.left, 1)
    time.sleep(0.3)
    press_1()
    time.sleep(0.3)
    mouseInput.position = (x, y)
    mouseInput.click(Button.left, 1)

def click_center():
    mouseInput.position = (wak_center_x, wak_center_y)
    mouseInput.click(Button.left, 1)

def click_close():
    mouseInput.position = (close_x, close_y)
    mouseInput.click(Button.left, 1)

def press_space():
    keyInput.press(' ')
    keyInput.release(' ')

def press_1():
    keyInput.press('&')
    keyInput.release('&')

# ----------------------------------------

# cat coords -------
# watch 22 up and down, 45 left and right

iter = 0

cat_down_x = 1210
cat_down_y = 732

cat_leftdown_x = 1150
cat_leftdown_y = 702

cat_left_x = 1090
cat_left_y = 674

cat_leftup_x = 1148
cat_leftup_y = 643

cat_up_x = 1209
cat_up_y = 614

cat_rightup_x = 1269
cat_rightup_y = 644

cat_right_x = 1326
cat_right_y = 673

cat_rightdown_x = 1268
cat_rightdown_y = 701

# character coords -

char_down_x = cat_down_x - 295
char_down_y = cat_down_y - 149

char_leftdown_x = cat_leftdown_x - 295
char_leftdown_y = cat_leftdown_y - 149

char_left_x = cat_left_x - 295
char_left_y = cat_left_y - 149

char_leftup_x = cat_leftup_x - 295
char_leftup_y = cat_leftup_y - 149

char_up_x = cat_up_x - 295
char_up_y = cat_up_y - 149

char_rightup_x = cat_rightup_x - 295
char_rightup_y = cat_rightup_y - 149

char_right_x = cat_right_x - 295
char_right_y = cat_right_y - 149

char_rightdown_x = cat_rightdown_x - 295
char_rightdown_y = cat_rightdown_y - 149

# ------------------

def remove_noise(screen):
    pic = []
    for i in range(1080):
        sub = []
        for j in range(1920):
            sub.append(0)
        pic.append(sub)
    for i in range(1920):
        for j in range(1080):
            (r, g, b) = screen.getpixel((i, j))
            if r == 255:
                pic[j][i] = 255

    for i in range(700, 1500):
        for j in range(400, 800):
            siblings = 0
            if pic[j][i] == pic[j + 1][i]:
                siblings += 1
            if pic[j][i] == pic[j - 1][i]:
                siblings += 1
            if pic[j][i] == pic[j][i + 1]:
                siblings += 1
            if pic[j][i] == pic[j][i - 1]:
                siblings += 1
            if pic[j][i] == pic[j + 1][i + 1]:
                siblings += 1
            if pic[j][i] == pic[j - 1][i - 1]:
                siblings += 1
            if pic[j][i] == pic[j - 1][i + 1]:
                siblings += 1
            if pic[j][i] == pic[j + 1][i - 1]:
                siblings += 1
            
            if siblings <= 2:
                if pic[j][i] == 0:
                    pic[j][i] = 255
                else:
                    pic[j][i] = 0

    for i in range(1182, 1195):
        for j in range(660, 675):
            pic[j][i] = 0
    
    '''
    img = Image.new('RGB', [1920,1080], 255)
    data = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            data[x,y] = (pic[y][x], pic[y][x], pic[y][x])

    img.save('C:/Users/abarb/Desktop/img.bmp')
    '''

    return pic

def diff(a, b):
    diff = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                diff += 1
    return diff

def get_square(pic, x, y):
    square = []
    for i in range(44):
        sub = []
        for j in range(70):
            sub.append(0)
        square.append(sub)
    y = y - 22
    for i in range(44):
        for j in range(35):
            square[i][35 + j] = pic[y + i][x + j]
            square[i][35 - j] = pic[y + i][x - j]
    return square

def choose(x, y):
    screen = pyautogui.screenshot()
    pic = remove_noise(screen)
    own_square = get_square(pic, x, y)

    d_diff = diff(own_square, get_square(pic, char_down_x, char_down_y))
    ld_diff = diff(own_square, get_square(pic, char_leftdown_x, char_leftdown_y))
    l_diff = diff(own_square, get_square(pic, char_left_x, char_left_y))
    lu_diff = diff(own_square, get_square(pic, char_leftup_x, char_leftup_y))
    u_diff = diff(own_square, get_square(pic, char_up_x, char_up_y))
    ru_diff = diff(own_square, get_square(pic, char_rightup_x, char_rightup_y))
    r_diff = diff(own_square, get_square(pic, char_right_x, char_right_y))
    rd_diff = diff(own_square, get_square(pic, char_rightdown_x, char_rightdown_y))

    min = d_diff
    if (ld_diff < min):
        min = ld_diff
    if (l_diff < min):
        min = l_diff
    if (lu_diff < min):
        min = lu_diff
    if (u_diff < min):
        min = u_diff
    if (ru_diff < min):
        min = ru_diff
    if (r_diff < min):
        min = r_diff
    if (rd_diff < min):
        min = rd_diff

    if min == d_diff:
        three_captchat_clicks_at(char_down_x, char_down_y)
    if min == ld_diff:
        three_captchat_clicks_at(char_leftdown_x, char_leftdown_y)
    if min == l_diff:
        three_captchat_clicks_at(char_left_x, char_left_y)
    if min == lu_diff:
        three_captchat_clicks_at(char_leftup_x, char_leftup_y)
    if min == u_diff:
        three_captchat_clicks_at(char_up_x, char_up_y)
    if min == ru_diff:
        three_captchat_clicks_at(char_rightup_x, char_rightup_y)
    if min == r_diff:
        three_captchat_clicks_at(char_right_x, char_right_y)
    if min == rd_diff:
        three_captchat_clicks_at(char_rightdown_x, char_rightdown_y)

    time.sleep(0.3)

def is_cross(pic, x, y):
    '''
    img = Image.open('C:/Users/abarb/Desktop/img.bmp')
    data = img.load()
    '''

    total = 0
    for i in range(22):
        #data[x,y + i] = (data[x,y + i][0], data[x,y + i][1], 128)
        #data[x,y - i] = (data[x,y - i][0], data[x,y - i][1], 128)
        if pic[y + i][x] != 255:
            total += 1
        if pic[y - i][x] != 255:
            total += 1

    if total == 0:
        #img.save('C:/Users/abarb/Desktop/img.bmp')
        return True
    
    x += 3
    total = 0
    for i in range(22):
        #data[x,y + i] = (data[x,y + i][0], data[x,y + i][1], 128)
        #data[x,y - i] = (data[x,y - i][0], data[x,y - i][1], 128)
        if pic[y + i][x] != 255:
            total += 1
        if pic[y - i][x] != 255:
            total += 1
    
    if total == 0:
        #img.save('C:/Users/abarb/Desktop/img.bmp')
        return True

    x += 2
    total = 0
    for i in range(22):
        #data[x,y + i] = (data[x,y + i][0], data[x,y + i][1], 128)
        #data[x,y - i] = (data[x,y - i][0], data[x,y - i][1], 128)
        if pic[y + i][x] != 255:
            total += 1
        if pic[y - i][x] != 255:
            total += 1
    
    if total == 0:
        #img.save('C:/Users/abarb/Desktop/img.bmp')
        return True

    x -= 8
    total = 0
    for i in range(22):
        #data[x,y + i] = (data[x,y + i][0], data[x,y + i][1], 128)
        #data[x,y - i] = (data[x,y - i][0], data[x,y - i][1], 128)
        if pic[y + i][x] != 255:
            total += 1
        if pic[y - i][x] != 255:
            total += 1

    if total == 0:
        #img.save('C:/Users/abarb/Desktop/img.bmp')
        return True

    x -= 2
    total = 0
    for i in range(22):
        #data[x,y + i] = (data[x,y + i][0], data[x,y + i][1], 128)
        #data[x,y - i] = (data[x,y - i][0], data[x,y - i][1], 128)
        if pic[y + i][x] != 255:
            total += 1
        if pic[y - i][x] != 255:
            total += 1

    if total == 0:
        #img.save('C:/Users/abarb/Desktop/img.bmp')
        return True

    #img.save('C:/Users/abarb/Desktop/img.bmp')
    return False

# on regarde le rouge, si c'est pas 255 alors c'est noir, sinon blanc
# puis si il est connecté à un seul pixel de son type, alors il est de l'autre type
def resolve_captchat():
    click_center()
    time.sleep(4)
    for i in range(25):
        press_space()
        time.sleep(0.25)
    time.sleep(4)
    # removing noise
    screen = pyautogui.screenshot()
    pic = remove_noise(screen)
    # checking crosses
    crosses = 0
    d, ld, l, lu, u, ru, r, rd = 0, 0, 0, 0, 0, 0, 0, 0
    if is_cross(pic, cat_down_x, cat_down_y) and crosses < 5:
        d = -1
        crosses += 1
    if is_cross(pic, cat_leftdown_x, cat_leftdown_y) and crosses < 5:
        ld = -1
        crosses += 1
    if is_cross(pic, cat_left_x, cat_left_y) and crosses < 5:
        l = -1
        crosses += 1
    if is_cross(pic, cat_leftup_x, cat_leftup_y) and crosses < 5:
        lu = -1
        crosses += 1
    if is_cross(pic, cat_up_x, cat_up_y) and crosses < 5:
        u = -1
        crosses += 1
    if is_cross(pic, cat_rightup_x, cat_rightup_y) and crosses < 5:
        ru = -1
        crosses += 1
    if is_cross(pic, cat_right_x, cat_right_y) and crosses < 5:
        r = -1
        crosses += 1
    if is_cross(pic, cat_rightdown_x, cat_rightdown_y) and crosses < 5:
        rd = -1
        crosses += 1

    print("CROSSES : " + str(crosses))
    if crosses != 5:
        print("ERROR, WRONG NUMBER OF CROSSES")
        exit(1)

    if d != -1:
        choose(cat_down_x, cat_down_y)
    if ld != -1:
        choose(cat_leftdown_x, cat_leftdown_y)
    if l != -1:
        choose(cat_left_x, cat_left_y)
    if lu != -1:
        choose(cat_leftup_x, cat_leftup_y)
    if u != -1:
        choose(cat_up_x, cat_up_y)
    if ru != -1:
        choose(cat_rightup_x, cat_rightup_y)
    if r != -1:
        choose(cat_right_x, cat_right_y)
    if rd != -1:
        choose(cat_rightdown_x, cat_rightdown_y)

def is_captchat():

    wait_time = 3.2

    while (wait_time > 0):
        total = 0
        screenshot = pyautogui.screenshot()
        (r, g, b) = screenshot.getpixel((960 + 0, 540 + 0))
        total += (r + g + b)/3
        (r, g, b) = screenshot.getpixel((960 + 100, 540 + 0))
        total += (r + g + b)/3
        (r, g, b) = screenshot.getpixel((960 - 100, 540 + 0))
        total += (r + g + b)/3
        (r, g, b) = screenshot.getpixel((960 + 0, 540 + 100))
        total += (r + g + b)/3
        (r, g, b) = screenshot.getpixel((960 + 0, 540 - 100))
        total += (r + g + b)/3
        (r, g, b) = screenshot.getpixel((960 + 100, 540 + 100))
        total += (r + g + b)/3
        (r, g, b) = screenshot.getpixel((960 - 100, 540 - 100))
        total += (r + g + b)/3
        (r, g, b) = screenshot.getpixel((960 + 100, 540 - 100))
        total += (r + g + b)/3
        (r, g, b) = screenshot.getpixel((960 - 100, 540 + 100))
        total += (r + g + b)/3

        total = total / 9
        
        if total < 15:
            print("--------")
            print("CAPTCHAT")
            print("--------")
            iter = 0
            resolve_captchat()
            time.sleep(4)
            click_close()
            time.sleep(0.5)


        time.sleep(0.1)
        wait_time -= 0.1
    
    return False