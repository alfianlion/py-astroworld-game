from Game import *
from MainMenu import *
from Story import *
from os import system, name

if __name__ == "__main__":
    Game.state = True
    Game.os = name
    Game.system = system
    while Game.state == True:
        if Story.storyState == False:
            MainMenu.welcomeMessage(Game.gameMenu)
            Game.option = input("\nSelect your option: ")
            Game.gameOption(Game.option)
        