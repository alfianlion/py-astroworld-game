from Story import *

class MainMenu:

    optionMenu = { '1':'Start New World', '2':'How to play & Credits', '0':'Exit Game' }
    option = ""

    def welcomeMessage(Util : any, optionMenu : dict):
        print('Welcome to AstroWorld!\n')
        for key, value in optionMenu.items():
            print(key + ")" + value)

    def menuOption(Util, option):
        match option:
            case "1":
                Util.clearTerminal(Util.os)
                Story.initStory(Util)
            case "2":
                Util.clearTerminal(Util.os)
                MainMenu.gameTutorial()
                MainMenu.gameCredits()
            case "0":
                print("Existing...")
                MainMenu.exitGame(Util)
            case _:
                Util.clearTerminal(Util.os)
                print("Option not selected. Try again.\n")

    def gameTutorial():
        return print("\n============================ How to Play? ============================\n\nGuess the words that are missing in the sentence.\nYou are able to guess the letters but you have a total of 5 tries.\nYou may guess the word if you know the word.\n\n======================================================================\n")
    
    def gameCredits():
        return print("\n============================ Credits =================================\n\nDeveloper: Alfian\nLangauge Used: Python\nGithub Repo: https://github.com/alfianlion/py-astroworld-game/\n\n======================================================================\n")  

    def exitGame(Util):
        Util.isLauncherRunning = False
        return Util.isLauncherRunning