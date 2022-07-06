# Age of Empire
[![wakatime](https://wakatime.com/badge/user/9657174f-2430-4dfd-aaef-2b316eb71a36/project/f7d62cf0-5f0f-4235-913f-4e393bb5bf20.svg)](https://wakatime.com/badge/user/9657174f-2430-4dfd-aaef-2b316eb71a36/project/f7d62cf0-5f0f-4235-913f-4e393bb5bf20)

A simple program to launch and automatically enter the license/activation 
code for Age Of Empire III to play the game.

## CheatEngine
A simple keystroke listener to catch specific hotkeys and run some cheat codes.

## SETUP
### Create a virtual environment
```commandline
$ python3 -m venv age_of_empire
```
### Activate virtual environment

```commandline
$ cd age_of_empire\Scripts\
$ activate
```

### Install the required dependencies
```commandline
(age_of_empire)$ pip install -r requirements.txt
```

## USAGE
### Run the game auto launcher
```commandline
(age_of_empire)$ python3 open_age_of_empire.py 
```

### Run the listener
```commandline
(age_of_empire)$ python3 listener.py 
```
### Cheats Hot Keys:
- Food 100,000 - `ctrl [`
- Wood 100,000 - `ctrl ]`
- Coins 100,000 - `ctrl ;`
- Laser Panda - `ctrl '`

To shut the listener down press *"."* 

## NOTE
The game has to be installed in this directory
```jsonpath
C:\"Program Files (x86)"\"Microsoft Studios"\"Age of Empires III - Complete"
```
in order to work properly. Installation path flexibility will be considered 
in the future
