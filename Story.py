from Storyline import *

class Story:
    #TODO: Hangman
    #1. Create a list of words that players are allowed to guess
    #2. Loop through the list and display it (before working on logic)
    #3. Randomize a selected word from the list
    #REMINDER: Story should be in third person

    playerName = ""
    antagonistName = ""
    storyState = False
    setupState = False
    wordList = ['search']

    def initStory(Game):
        Story.setupState = True
        Storyline.initStoryline("fullstory.txt")
        print("Hi, Welcome to AstroWorld Arena. Before we begin, we would like to your name!")
        while Story.setupState == True:    
            Story.playerName = input("Whats your name?  ")
            print(Story.playerName + "? is that really you?")
            Game.option = input("Enter 'y' to continue, 'n' to restart: ")
            match Game.option.lower():
                case 'y':
                    Game.option = ""
                    Game.clearTerminal(Game.os)
                    Story.antagonistName = input("Who is that someone that you deem as a Rival of your life? ")
                    print(Story.antagonistName + " is your rival?")
                    Game.option = input("Enter 'y' to continue, 'n' to restart: ")
                    match Game.option.lower():
                        case 'y':
                            Story.storyState = True
                            Story.setupState = False
                            return Story.storyIntro(Game)
                        case 'n':
                            Game.clearTerminal(Game.os)   
                            continue
                        case _:
                            print("Invalid option. Please enter 'y' or 'n'.")
                case 'n':
                    Game.clearTerminal(Game.os)   
                    continue
                case _:
                    print("Invalid option. Please enter 'y' or 'n'.")

    def storyIntro(Game):
            if Story.storyState == True:
                Game.clearTerminal(Game.os)
                Story.toString()
                Storyline.toPartStory('Intro')
    
    def storyTutorial():
        return print("\n============================ How to Play? ============================\n\nGuess the words that are missing in the sentence.\nYou are able to guess the letters but you have a total of 5 tries.\nYou may guess the word if you know the word.\n\n======================================================================\n")
    
    def storyCredits():
        return print("\n============================ Credits =================================\n\nDeveloper: Alfian\nLangauge Used: Python\nGithub Repo: https://github.com/alfianlion/py-astroworld-game/\n\n======================================================================\n")

    def toString():
        return print("Player Name:", Story.playerName, "\nAntagonist Name:", Story.antagonistName, "\nStory State:", Story.storyState, "\nSetup State:",Story.setupState)