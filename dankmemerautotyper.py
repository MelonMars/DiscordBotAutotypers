import pyautogui as pg
import pyperclip as pc
import time

time.sleep(2)
def main():
    pc.copy("pls beg")
    pg.hotkey("ctrl", "v")
    pg.press("enter")
    time.sleep(45)

for i in range(3):
    main()