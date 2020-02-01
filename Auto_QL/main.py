# 自动登录
# wegame登录按钮坐标1200，618
#
import pyautogui
import time


while True:
    dl = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL/a10.png', confidence=0.9)  # 游戏退出，wegame在桌面
    jryx = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL/a3.png', confidence=0.9)  # 选择橘色页面
    if dl:
        pyautogui.moveTo(1200, 618)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    elif jryx:
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
    time.sleep(60)

