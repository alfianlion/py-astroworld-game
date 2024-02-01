from Story import *

class Game:
    state = False
    gameMenu = { '1':'Start New World', '2':'How to play & Credits', '0':'Exit Game' }
    option = ""
    os = ""
    system = any

    def gameOption(option):
        match option:
            case "1":
                Game.clearTerminal(Game.os)
                Story.initStory(Game)
            case "2":
                Game.clearTerminal(Game.os)
                Story.storyTutorial()
                Story.storyCredits()
            case "0":
                print("Existing...")
                Game.exitGame()
            case _:
                Game.clearTerminal(Game.os)
                print("Option not selected. Try again.\n")
            
    def exitGame():
        Game.state = False
        return Game.state

    def clearTerminal(os):
        if os == 'cls':
            _ = Game.system('cls')
        else:
            _ = Game.system('clear')