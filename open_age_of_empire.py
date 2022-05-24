import pyautogui
import os
import threading
import time


# function to open age of empire
def age_of_empire():
    # run the apps the app and waits for code entry
    def run_app():
        os.system("cls")
        print("Opening the app")
        os.system('C:\\"Program Files (x86)"\\"Microsoft Studios"\\"Age of Empires III - Complete '
                  'Collection"\\bin\\age3.exe')

    # writes the activation code
    def write_code():
        os.system("cls")
        print("writing code........")
        time.sleep(5)
        # pyautogui.moveTo(523,402)
        # pyautogui.click()

        pyautogui.write("PTMGF28VKB2W934482QH98623", interval=0.25)
        pyautogui.press('enter')

    # multi threads the process... (runs each of the functions as different processes)
    th1 = threading.Thread(target=run_app)
    th2 = threading.Thread(target=write_code)
    th1.start()
    th2.start()


# runs the app without writing the activation code
def age_of_empire_codeless():
    os.system("cls")
    print("Opening the app")
    os.system(
        'C:\\"Program Files (x86)"\\"Microsoft Studios"\\"Age of Empires III - Complete Collection"\\bin\\age3.exe')


# function to open asian dynasties
def asian_dynasties():
    # run the apps the app and waits for code entry
    def run_app():
        os.system("cls")
        print("Opening the app")
        os.system(
            'C:\\"Program Files (x86)"\\"Microsoft Studios"\\"Age of Empires III - Complete Collection"\\bin\\age3y.exe')

    # writes the activation code
    def write_code():
        os.system("cls")
        print("writing code........")
        time.sleep(5)
        # pyautogui.moveTo(523,402)
        # pyautogui.click()
        pyautogui.write("QRR4PF4FDPH986RRF6P37QK3R", interval=0.25)
        pyautogui.press('enter')

    # multi threads the process... (runs each of the functions as different processes)
    th1 = threading.Thread(target=run_app)
    th2 = threading.Thread(target=write_code)
    th1.start()
    th2.start()


# runs app without writing the code
def asian_dynasties_codeless():
    os.system("cls")
    print("Opening the app")
    os.system(
        'C:\\"Program Files (x86)"\\"Microsoft Studios"\\"Age of Empires III - Complete Collection"\\bin\\age3y.exe')


def warchiefs():
    # run the apps the app and waits for code entry
    def run_app():
        os.system("cls")
        print("Opening the app")
        os.system(
            'C:\\"Program Files (x86)"\\"Microsoft Studios"\\"Age of Empires III - Complete Collection"\\bin\\age3x.exe')

    # writes the activation code
    def write_code():
        os.system("cls")
        print("writing code........")
        time.sleep(5)
        # pyautogui.moveTo(523,402)
        # pyautogui.click()
        pyautogui.write("KJG93HDPGBPXBPPTFB499DBVB", interval=0.25)
        pyautogui.press('enter')

    # multi threads the process... (runs each of the functions as different processes)
    th1 = threading.Thread(target=run_app)
    th2 = threading.Thread(target=write_code)
    th1.start()
    th2.start()


def warchiefs_codeless():
    os.system("cls")
    print("Opening the app")
    os.system(
        'C:\\"Program Files (x86)"\\"Microsoft Studios"\\"Age of Empires III - Complete Collection"\\bin\\age3x.exe')


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
            age_of_empire()
        elif userInput == "2":
            age_of_empire_codeless()

    elif (userInput == "2"):
        # asian_dynasties
        os.system("cls")
        print("1. Run with activation code\n2. Run without activation code")
        userInput = input()

        if userInput == "1":
            asian_dynasties()
        elif userInput == "2":
            asian_dynasties_codeless()

    elif (userInput == "3"):
        # warchiefs
        os.system("cls")
        print("1. Run with activation code\n2. Run without activation code")
        userInput = input()

        if userInput == "1":
            warchiefs()
        elif userInput == "2":
            warchiefs_codeless()
    else:
        print("invalid input")


if __name__ == "__main__":
    main()
