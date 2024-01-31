
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

    def storyIntro(Game):
        Game.clearTerminal(Game.os)
        Story.toString()

    def initStory(Game):
        Story.setupState = True
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
                            Story.storyIntro(Game)
                            Story.storyState = True
                            Story.setupState = False
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

    def toString():
        return print("Player Name:", Story.playerName, "\nAntagonist Name:", Story.antagonistName, "\nStory State:", Story.storyState, "\nSetup State:",Story.setupState)