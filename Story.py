from Storyline import *

class Story:
    

    playerName = ""
    antagonistName = ""
    storyState = False
    setupState = False
    option = ""
    wordList = ['struggling','average', 'mocked',
                'awestruck','ignited','determination',
                'train','studying','awareness',
                'setbacks','manage','strength',
                'astonished','friends','dream',
                'victory','dedication','self-belief']

    def initStory(Util):
        Story.setupState = True
        Storyline.initStoryline("fullstory.txt")
        print("Hi, Welcome to AstroWorld Arena. Before we begin, we would like to your name!")
        while Story.setupState == True:    
            Story.playerName = input("Whats your name?  ")
            print(Story.playerName + "? is that really you?")
            Story.option = input("Enter 'y' to continue, 'n' to restart: ")
            match Story.option.lower():
                case 'y':
                    Story.option = ""
                    Util.clearTerminal(Util.os)
                    Story.antagonistName = input("Who is that someone that you deem as a Rival of your life? ")
                    print(Story.antagonistName + " is your rival?")
                    Story.option = input("Enter 'y' to continue, 'n' to restart: ")
                    match Story.option.lower():
                        case 'y':
                            Story.storyState = True
                            Story.setupState = False
                            return Story.storyStart(Util)
                        case 'n':
                            Util.clearTerminal(Util.os)   
                            continue
                        case _:
                            Util.clearTerminal(Util.os)   
                            print("Invalid option. Please enter 'y' or 'n'.")
                case 'n':
                    Util.clearTerminal(Util.os)   
                    continue
                case _:
                    Util.clearTerminal(Util.os)   
                    print("Invalid option. Please enter 'y' or 'n'.")

    def storyStart(Util):
        Story.toString()
        Story.storyIntro(Util)
        Story.storyTrigger(Util)
        Story.storyJourney(Util)
        Story.storyTrials(Util)
        Story.storyClimax(Util)
        Story.storyConclusion(Util)
    
    def storyIntro(Util):
            if Story.storyState == True:
                Util.clearTerminal(Util.os)
                Storyline.toPartStory('Intro')
                input("\nEnter any button to continue")
    
    def storyTrigger(Util):
            if Story.storyState == True:
                Util.clearTerminal(Util.os)
                Storyline.toPartStory('Trigger')
                input("\nEnter any button to continue")
          

    def storyJourney(Util):
            if Story.storyState == True:
                Util.clearTerminal(Util.os)
                Storyline.toPartStory('Journey')
                input("\nEnter any button to continue")

    def storyTrials(Util):
            if Story.storyState == True:
                Util.clearTerminal(Util.os)
                Storyline.toPartStory('Trials')
                input("\nEnter any button to continue")

    
    def storyClimax(Util):
            if Story.storyState == True:
                Util.clearTerminal(Util.os)
                Storyline.toPartStory('Climax')
                input("\nEnter any button to continue")
    
    def storyConclusion(Util):
            if Story.storyState == True:
                Util.clearTerminal(Util.os)
                Storyline.toPartStory('Conclusion')
                input("\nEnter any button to continue\n")
                Story.storyState = False

    def toString():
        return print("Player Name:", Story.playerName, "\nAntagonist Name:", Story.antagonistName, "\nStory State:", Story.storyState, "\nSetup State:",Story.setupState)