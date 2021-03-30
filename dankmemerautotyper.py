import pyautogui as pg
import pyperclip as pc
import time

reps = int(input("How many reps? "))
time.sleep(2)

def main():
    pc.copy("pls beg")
    pg.hotkey("ctrl", "v")
    pg.press("enter")
    pc.copy("pls fish")
    pg.hotkey("ctrl", "v")
    pg.press("enter")
    pc.copy("pls hl")
    pg.hotkey("ctrl", "v")
    pg.press("enter")
    pc.copy("high")
    pg.hotkey("ctrl", "v")
    pg.press("enter")
    time.sleep(45)
    pc.copy("pls pm")
    pg.hotkey("ctrl", "v")
    pg.press("enter")
    pc.copy("f")
    pg.hotkey("ctrl", "v")
    pg.press("enter")
    pc.copy("pls search")
    pg.hotkey("ctrl", "v")
    pg.press("enter")
    pc.copy("air")
    pg.hotkey("ctrl", "v")
    pg.press("enter")

for i in range(reps):
    main()
    