from CheatEngine import CheatEngine as ce
import keyboard


def addHotKeys():
    keyboard.add_hotkey("ctrl+[", lambda: ce.foodCheat())
    keyboard.add_hotkey("ctrl+]", lambda: ce.coinsCheat())
    keyboard.add_hotkey("ctrl+;", lambda: ce.woodCheat())
    keyboard.add_hotkey("ctrl+'", lambda: ce.pandaCheat())


def main():
    addHotKeys()

    print("Cheat server started!\n")
    print("=========Hot Keys=========")
    print("Food 100,000 - ctrl f \nWood 100,000 - ctrl w \nCoins 100,000 - ctrl c "
          "\nLaser Panda - ctrl p \nPress \".\" to shut the listener down\n")
    print("Listening to keystroke.......")

    keyboard.wait(".")
    print("Shutting server down")


if __name__ == "__main__":
    main()
