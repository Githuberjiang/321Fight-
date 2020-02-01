# 检测疲劳
# 换角色
# 移动至副本
# 自动攻击
# 拾取
# 再次挑战


import pyautogui
import random
import time

l = ['a', 's', 'd', 'q', 'w', 'e', 'f']
a = 0
t1 = time.time()
f = 'right'


def pljc():
    pl = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL/a5.png', confidence=0.95)  # 疲劳值为空的判断
    plex = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL/a4.png', confidence=0.95)  # ex空疲劳
    time.sleep(1.33)
    if pl or plex:
        change_role()
    else:
        move_to()


def change_role():
    global a
    a += 1
    while True:
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        time.sleep(random.random())
        pyautogui.moveTo(622, 533)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(1.33)
        xzjs = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL/a3.png', confidence=0.9)  # 选择角色页面
        time.sleep(1.33)
        if xzjs:
            if a > 12:
                a = 0
                pyautogui.moveTo(826, 656)
                time.sleep(random.random())
                pyautogui.mouseDown()
                pyautogui.mouseUp()
            pyautogui.keyDown(f)
            pyautogui.keyUp(f)
            time.sleep(random.random())
            for i in range(2):
                pyautogui.keyDown('space')
                pyautogui.keyUp('space')
            time.sleep(5)
            move_to()
            break


def move_to():
    pl = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL/a5.png', confidence=0.95)  # 疲劳值为空的判断
    time.sleep(1)
    if pl:
        change_role()
    else:
        pyautogui.keyDown('down')
        time.sleep(2.33)
        pyautogui.keyUp('down')
        pyautogui.keyDown('n')
        pyautogui.keyUp('n')
        time.sleep(0.33)
        for i in range(2):
            pyautogui.moveTo(618, 314)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        time.sleep(6.66)
        pyautogui.keyDown('n')
        pyautogui.keyUp('n')
        time.sleep(0.33)
        pyautogui.keyDown("up")
        time.sleep(0.33)
        pyautogui.keyUp("up")
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        time.sleep(0.33)
        pyautogui.keyDown("down")
        pyautogui.keyUp("down")
        time.sleep(0.33)
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        time.sleep(0.33)
        pyautogui.keyDown("a")
        pyautogui.keyUp("a")
        time.sleep(0.33)
        pyautogui.keyDown("enter")
        pyautogui.keyUp("enter")
        time.sleep(1)
        pyautogui.keyDown("down")
        time.sleep(1)
        pyautogui.keyUp("down")
        pyautogui.keyDown("right")
        time.sleep(3)
        pyautogui.keyUp("right")
        time.sleep(1)
        for i in range(2):
            pyautogui.moveTo(353, 536)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.keyDown("space")
            pyautogui.keyUp("space")
            pyautogui.moveTo(838, 487)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.keyDown("space")
            pyautogui.keyUp("space")
        time.sleep(1)
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')


def auto_attack():
    for i in range(2):
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("x")
        time.sleep(1.23 + random.random())
        pyautogui.keyUp("x")
        pyautogui.keyDown("x")
        pyautogui.keyDown("r")
        pyautogui.keyUp("r")
        p = random.choices(l)[0]
        q = random.choices(l)[0]
        o = random.choices(l)[0]
        pyautogui.keyDown(p)
        pyautogui.keyUp(p)
        pyautogui.keyDown(q)
        pyautogui.keyUp(q)
        pyautogui.keyDown(o)
        pyautogui.keyUp(o)
        pyautogui.keyUp("x")


def pickup():
    pyautogui.keyDown('ctrlleft')
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyDown('ctrl')
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.keyUp('ctrl')
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    pyautogui.keyDown('x')
    time.sleep(3 + random.random())
    pyautogui.keyUp('x')
    one_more()


def one_more():
    for i in range(2):
        pyautogui.keyDown('f10')
        pyautogui.keyUp('f10')
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    time.sleep(0.33)
    pyautogui.keyDown('f12')
    pyautogui.keyUp('f12')


while True:
    sfjx = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL/a8.png', confidence=0.9)  # 是否可以再次挑战
    cz = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL/a2.png', confidence=0.9)  # 在城镇
    jryx = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL/a3.png', confidence=0.9)  # 选择橘色页面
    time.sleep(1)
    t2 = time.time()
    if t2 - t1 > 30:
        t1 = time.time()
        right = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL/a6.png', confidence=0.8)  # 向右换角色
        left = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL/a9.png', confidence=0.8)  # 向左换角色
        dl = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL/a10.png', confidence=0.9)  # wegame在桌面
        time.sleep(2)
        if dl:
            pyautogui.moveTo(1200, 618)
            time.sleep(random.random())
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(180)
            pyautogui.moveTo(656, 656)
            time.sleep(random.random())
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(2)
            move_to()
        elif right:
            f = 'right'
            print(f)
        elif left:
            f = 'left'
            print(f)
    elif jryx:
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        time.sleep(2)
        move_to()
    elif sfjx:
        pickup()
    elif cz:
        pyautogui.mouseDown('down')
        time.sleep(2)
        pyautogui.mouseUp('down')
        pljc()
    try:
        auto_attack()
    except:
        pyautogui.moveTo(1280 / 2, 720 / 2)
        print('hh')
        time.sleep(60)
