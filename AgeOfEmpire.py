import pyautogui
import os
import threading
import time


class AgeOfEmpire:
    def __init__(self):
        pass

    # function to open age of empire
    @staticmethod
    def age_of_empire():
        # run the apps and waits for code entry
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

            pyautogui.write("PTMGF28VKB2W934482QH98623", interval=0.25)
            pyautogui.press('enter')

        # multi threads the process... (runs each of the functions as different processes)
        th1 = threading.Thread(target=run_app)
        th2 = threading.Thread(target=write_code)
        th1.start()
        th2.start()

    # function to run age of empire without writing the activation code
    @staticmethod
    def age_of_empire_codeless():
        os.system("cls")
        print("Opening the app")
        os.system(
            'C:\\"Program Files (x86)"\\"Microsoft Studios"\\"Age of Empires III - Complete Collection"\\bin\\age3.exe')

    # function to open asian dynasties
    @staticmethod
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

            pyautogui.write("QRR4PF4FDPH986RRF6P37QK3R", interval=0.25)
            pyautogui.press('enter')

        # multi threads the process... (runs each of the functions as different processes)
        th1 = threading.Thread(target=run_app)
        th2 = threading.Thread(target=write_code)
        th1.start()
        th2.start()

    # function to open asian dynasties without writing the activation code
    @staticmethod
    def asian_dynasties_codeless():
        os.system("cls")
        print("Opening the app")
        os.system(
            'C:\\"Program Files (x86)"\\"Microsoft Studios"\\"Age of Empires III - Complete Collection"\\bin\\age3y.exe')

    # function to open war chiefs
    @staticmethod
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

            pyautogui.write("KJG93HDPGBPXBPPTFB499DBVB", interval=0.25)
            pyautogui.press('enter')

        # multi threads the process... (runs each of the functions as different processes)
        th1 = threading.Thread(target=run_app)
        th2 = threading.Thread(target=write_code)
        th1.start()
        th2.start()

    # function to open war chiefs without writing the activation code
    @staticmethod
    def warchiefs_codeless():
        os.system("cls")
        print("Opening the app")
        os.system(
            'C:\\"Program Files (x86)"\\"Microsoft Studios"\\"Age of Empires III - Complete Collection"\\bin\\age3x.exe')

