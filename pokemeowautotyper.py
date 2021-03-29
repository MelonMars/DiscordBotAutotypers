import pyperclip as pc
import pyautogui as pg
import time

reps = int(input("How many iterations? "))
pokeballs = int(input("How many pokeballs do you currently have? "))
print("WARNING! If you have too little money to buy more pokeballs, the bot will keep running!")

def main():
    for i in range(pokeballs):
        