from MainMenu import *
from Story import *
from Util import *
from os import system, name

if __name__ == "__main__":
    Util.isLauncherRunning = True
    Util.os = name
    Util.system = system
    while Util.isLauncherRunning == True:
        if Story.storyState == False:
            MainMenu.welcomeMessage(Util, MainMenu.optionMenu)
            MainMenu.option = input("\nSelect your option: ")
            MainMenu.menuOption(Util, MainMenu.option)
        