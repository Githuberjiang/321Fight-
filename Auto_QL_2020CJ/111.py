import pyautogui
import time
t1 = time.time()

pl = pyautogui.locateOnScreen('/Users/yi/Desktop/321Fight/Auto_QL_2020CJ/a2.png', confidence=0.95)  # 疲劳值为空的判断

print(pl, time.time()-t1)