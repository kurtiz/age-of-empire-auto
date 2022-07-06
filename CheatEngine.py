import pyautogui
import time


class CheatEngine:
    def __init__(self):
        pass

    @staticmethod
    def foodCheat():
        time.sleep(3)
        pyautogui.press("enter")
        pyautogui.write("Medium Rare Please", interval=0.25)
        pyautogui.press("enter")

    @staticmethod
    def coinsCheat():
        time.sleep(3)
        pyautogui.press("enter")
        pyautogui.write("Give me liberty or give me coin", interval=0.25)
        pyautogui.press("enter")

    @staticmethod
    def woodCheat():
        time.sleep(3)
        pyautogui.press("enter")
        pyautogui.write("<censored>", interval=0.25)
        pyautogui.press("enter")

    @staticmethod
    def pandaCheat():
        time.sleep(3)
        pyautogui.press("enter")
        pyautogui.write("o Canada 2005", interval=0.25)
        pyautogui.press("enter")
