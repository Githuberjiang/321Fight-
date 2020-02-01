import pyautogui
import time
import random
pm = pyautogui.moveTo
pl = pyautogui.locateOnScreen
pkd = pyautogui.keyDown
pku = pyautogui.keyUp
pmd = pyautogui.mouseDown
pmu = pyautogui.mouseUp
d = 'down'
s = 'space'
r = 'right'
l = 'left'


t = time.time
ts = time.sleep

rr = random.random

t1 = time.time()

def moveto():
    pass


def start_game():
    pm(111, 222)  # wegame启动按钮所在定位                                   ！！！！！
    ts(rr())
    pmd()
    pmu()
    ts(180)
    pm(pyautogui.size() / 5, pyautogui.size() / 5)
    pmd()
    pmu()
    pkd(s)
    pkd(s)
    ts(rr())
    pkd(d)
    ts(2)
    pku(d)

while True:
    if t() - t1 > 300:
        t1 = t()
        start_game = pl('qd.png', confidence=0.9)  # wegame启动
        if start_game:  # 屏幕中存在wegame启动按钮
            start_game()
            moveto()
    on_cz = pl('jdc.png', confidence=0.9)  # 根据决斗场图标检测角色是否在城镇中
    onemore = pl('fhcz.png', confidence=0.9) # 根据返回城镇字体检测Boos是否被消灭
    time.sleep(1.23)




