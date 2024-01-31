from Game import *
from MainMenu import *

if __name__ == "__main__":
    Game.state = True
    while Game.state == True:
        MainMenu.welcomeMessage(Game.gameMenu)
        Game.option = input("\nSelect your option: ")
        Game.gameOption(Game.option)