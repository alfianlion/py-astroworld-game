from newGame import *

class Game:
    state = False
    gameMenu = { '1':'Start New World', '2':'Credits', '0':'Exit Game' }
    option = ""

    def gameOption(option):
        match option:
            case "1":
                newGame.initGame()
            case "2":
                print("hello3")
            case "0":
                print("Existing...")
                Game.exitGame()
            case _:
                print("Option not selected. Try again")

    def exitGame():
        Game.state = False
        return Game.state