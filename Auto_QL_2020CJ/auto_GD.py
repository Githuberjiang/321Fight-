# 检测疲劳
# 换角色
# 移动至副本
# 自动攻击
# 拾取
# 再次挑战


import pyautogui
import random
import time


t1 = time.time()
sfjx = pyautogui.locateOnScreen('/Users/yi/Desktop/FORFND/auto_GD/a8.png', confidence=0.9)  # 再次挑战
cz = pyautogui.locateOnScreen('/Users/yi/Desktop/FORFND/auto_GD/a2.png', confidence=0.9)  # 在城镇

print(time.time()-t1)