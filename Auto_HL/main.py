# 检测地图
import pyautogui
import time


t1 = time.time()
o = pyautogui.locateOnScreen('22.png', confidence=0.9)
a = pyautogui.locateOnScreen('1.png', confidence=0.9)
if o[0] > a[0]:  # ？在右边
    pyautogui.keyDown('right')

# a = pyautogui.locateAllOnScreen('1.png', confidence=0.9)
# print(list(a))

pyautogui.keyDown('down')
print(time.time()-t1)
