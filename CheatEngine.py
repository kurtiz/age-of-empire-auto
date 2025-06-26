import pyautogui
import time
import pydirectinput


class CheatEngine:
    def __init__(self):
        pass

    @staticmethod
    def _pressEnter():
        """Helper method to press Enter more reliably"""
        # Try multiple methods to ensure Enter works
        pydirectinput.press("enter")  # Use pydirectinput for more reliable input
        time.sleep(0.1)  # Small delay to ensure the command is registered

    @staticmethod
    def giftFromTheGods(amount=None):
        """Gives you 100000 of each resource and advances all phases (with 'i am too busy' effect)"""
        time.sleep(3)
        CheatEngine._pressEnter()
        if amount:
            pyautogui.write(f"gift from the gods {amount}", interval=0.25)
        else:
            pyautogui.write("gift from the gods", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def getPizza(amount=None):
        """Gives you food. Default 1000 if no amount specified"""
        time.sleep(3)
        CheatEngine._pressEnter()
        if amount:
            pyautogui.write(f"i want pizza {amount}", interval=0.25)
        else:
            pyautogui.write("i want pizza", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def bringMyAxe(amount=None):
        """Gives you wood. Default 1000 if no amount specified"""
        time.sleep(3)
        CheatEngine._pressEnter()
        if amount:
            pyautogui.write(f"bring me my axe {amount}", interval=0.25)
        else:
            pyautogui.write("bring me my axe", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def yourMoneyOrLife(amount=None):
        """Gives you metal. Default 1000 if no amount specified"""
        time.sleep(3)
        CheatEngine._pressEnter()
        if amount:
            pyautogui.write(f"your money or your life {amount}", interval=0.25)
        else:
            pyautogui.write("your money or your life", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def seeMountainHere(amount=None):
        """Gives you stone. Default 1000 if no amount specified"""
        time.sleep(3)
        CheatEngine._pressEnter()
        if amount:
            pyautogui.write(f"i see a mountain here {amount}", interval=0.25)
        else:
            pyautogui.write("i see a mountain here", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def revealMap():
        """Reveals the entire map"""
        time.sleep(3)
        CheatEngine._pressEnter()
        pyautogui.write("jame jam", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def spawnHeroes(amount=None):
        """Gives you random heroes (requires building selected)"""
        time.sleep(3)
        CheatEngine._pressEnter()
        if amount:
            pyautogui.write(f"iwanttopwnthem {amount}", interval=0.25)
        else:
            pyautogui.write("iwanttopwnthem", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def convertUnit():
        """Converts the currently selected unit to belong to you"""
        time.sleep(3)
        CheatEngine._pressEnter()
        pyautogui.write("wololo", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def killUnit():
        """Kills the currently selected unit"""
        time.sleep(3)
        CheatEngine._pressEnter()
        pyautogui.write("black death", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def speedUp():
        """Speeds up action for your own buildings and units"""
        time.sleep(3)
        CheatEngine._pressEnter()
        pyautogui.write("i am too busy", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def spawnMustang():
        """Gives you P-51 Mustang plane (requires building selected)"""
        time.sleep(3)
        CheatEngine._pressEnter()
        pyautogui.write("how do you turn this on?", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def defeatPlayer(player_number=2):
        """Defeats specified player instantly. Default is player 2"""
        time.sleep(3)
        CheatEngine._pressEnter()
        if player_number != 2:
            pyautogui.write(f"exodia {player_number}", interval=0.25)
        else:
            pyautogui.write("exodia", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def spawnCitizenSoldier():
        """Gives you random citizen soldier (requires building selected)"""
        time.sleep(3)
        CheatEngine._pressEnter()
        pyautogui.write("salad bowl", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def advancePhase():
        """Advances to the next phase"""
        time.sleep(3)
        CheatEngine._pressEnter()
        pyautogui.write("back to the future", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def maxPopulation():
        """Increases population to maximum limit (300 by default)"""
        time.sleep(3)
        CheatEngine._pressEnter()
        pyautogui.write("the hive master", interval=0.25)
        CheatEngine._pressEnter()

    @staticmethod
    def increasePopulationLimit():
        """Increases the maximum population by 500"""
        time.sleep(3)
        CheatEngine._pressEnter()
        pyautogui.write("TARDIS", interval=0.25)
        CheatEngine._pressEnter()
        pyautogui.press("enter")

    @staticmethod
    def increasePopulationLimit():
        """Increases the maximum population by 500"""
        time.sleep(3)
        pyautogui.press("enter")
        pyautogui.write("TARDIS", interval=0.25)
        pyautogui.press("enter")
