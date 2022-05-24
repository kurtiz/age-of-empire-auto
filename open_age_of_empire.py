from AgeOfEmpire import AgeOfEmpire as aoe
import os


# main function
def main():
    print("Which version of Age of Empire III do you want to play?")
    print("1. Age of Empire III\n2. Asian Dynasties\n3. Warchief")
    userInput = input()

    if userInput == "1":
        # age_of_empire
        os.system("cls")
        print("1. Run with activation code\n2. Run without activation code")
        userInput = input()

        if userInput == "1":
            aoe.age_of_empire()
        elif userInput == "2":
            aoe.age_of_empire_codeless()

    elif (userInput == "2"):
        # asian_dynasties
        os.system("cls")
        print("1. Run with activation code\n2. Run without activation code")
        userInput = input()

        if userInput == "1":
            aoe.asian_dynasties()
        elif userInput == "2":
            aoe.asian_dynasties_codeless()

    elif (userInput == "3"):
        # warchiefs
        os.system("cls")
        print("1. Run with activation code\n2. Run without activation code")
        userInput = input()

        if userInput == "1":
            aoe.warchiefs()
        elif userInput == "2":
            aoe.warchiefs_codeless()
    else:
        print("invalid input")


if __name__ == "__main__":
    main()
