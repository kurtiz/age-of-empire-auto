from CheatEngine import CheatEngine as ce
import keyboard


def addHotKeys():
    keyboard.add_hotkey("ctrl+f", lambda: ce.foodCheat())
    keyboard.add_hotkey("ctrl+c", lambda: ce.coinsCheat())
    keyboard.add_hotkey("ctrl+w", lambda: ce.woodCheat())
    keyboard.add_hotkey("ctrl+p", lambda: ce.pandaCheat())


def main():
    addHotKeys()
    print(keyboard.get_hotkey_name())
    print("Cheat server started!")
    print("Listening to keystroke.......")
    keyboard.wait(".")


if __name__ == "__main__":
    main()
