from CheatEngine import CheatEngine as ce
import keyboard


def addHotKeys():
    # Resource cheats
    keyboard.add_hotkey("ctrl+1", lambda: ce.giftFromTheGods())  # All resources
    keyboard.add_hotkey("ctrl+2", lambda: ce.getPizza())        # Food
    keyboard.add_hotkey("ctrl+3", lambda: ce.bringMyAxe())      # Wood
    keyboard.add_hotkey("ctrl+4", lambda: ce.yourMoneyOrLife()) # Metal
    keyboard.add_hotkey("ctrl+5", lambda: ce.seeMountainHere()) # Stone
    
    # Map and vision
    keyboard.add_hotkey("ctrl+6", lambda: ce.revealMap())       # Reveal map
    
    # Unit spawning
    keyboard.add_hotkey("ctrl+7", lambda: ce.spawnHeroes())     # Spawn heroes
    keyboard.add_hotkey("ctrl+8", lambda: ce.spawnCitizenSoldier()) # Spawn citizen soldier
    keyboard.add_hotkey("ctrl+9", lambda: ce.spawnMustang())    # Spawn plane
    
    # Unit actions
    keyboard.add_hotkey("ctrl+q", lambda: ce.convertUnit())    # Convert unit
    keyboard.add_hotkey("ctrl+w", lambda: ce.killUnit())       # Kill unit
    
    # Game modifiers
    keyboard.add_hotkey("ctrl+e", lambda: ce.speedUp())        # Speed up
    keyboard.add_hotkey("ctrl+r", lambda: ce.advancePhase())   # Next phase
    keyboard.add_hotkey("ctrl+t", lambda: ce.maxPopulation()) # Max population
    keyboard.add_hotkey("ctrl+y", lambda: ce.increasePopulationLimit()) # Increase pop limit
    keyboard.add_hotkey("ctrl+u", lambda: ce.defeatPlayer())   # Defeat player 2


def main():
    addHotKeys()

    print("Cheat server started!\n")
    print("=========Hot Keys=========")
    print("RESOURCES:")
    print("Ctrl+1 - All Resources (Gift from Gods)")
    print("Ctrl+2 - Food (Pizza)")
    print("Ctrl+3 - Wood (Axe)")
    print("Ctrl+4 - Metal (Money or Life)")
    print("Ctrl+5 - Stone (Mountain)")
    print("\nMAP & VISION:")
    print("Ctrl+6 - Reveal Map")
    print("\nUNIT SPAWNING:")
    print("Ctrl+7 - Spawn Heroes")
    print("Ctrl+8 - Spawn Citizen Soldier")
    print("Ctrl+9 - Spawn P-51 Mustang")
    print("\nUNIT ACTIONS:")
    print("Ctrl+Q - Convert Unit (Wololo)")
    print("Ctrl+W - Kill Unit")
    print("\nGAME MODIFIERS:")
    print("Ctrl+E - Speed Up")
    print("Ctrl+R - Advance Phase")
    print("Ctrl+T - Max Population")
    print("Ctrl+Y - Increase Pop Limit")
    print("Ctrl+U - Defeat Player 2")
    print("\nPress \".\" to shut the listener down\n")
    print("Listening to keystroke.......")

    keyboard.wait(".")
    print("Shutting server down")


if __name__ == "__main__":
    main()