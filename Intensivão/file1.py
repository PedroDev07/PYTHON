import pyautogui
import pyperclip
import time 

pyautogui.PAUSE = 1
pyautogui.hotkey('win')

pyautogui.write('chrome')

pyautogui.press('enter')

pyautogui.hotkey('tab')

pyautogui.press('enter')

pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')

pyautogui.hotkey('ctrl','v')

pyautogui.press('enter')


time.sleep(4)
pyautogui.click(x=393, y=264, clicks=3)
time.sleep(4)
pyautogui.click(x=393, y=268, clicks=1)
time.sleep(4)
pyautogui.click(x=1158, y=161, clicks=1)
time.sleep(4)
pyautogui.click(x=984, y=556, clicks=1)
print(pyautogui.position())