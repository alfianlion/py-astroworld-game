class Storyline:
    storylineMain= {}

    def initStoryline(fileName:str):
        with open(fileName) as file:
            for lines in file:
                part = lines.strip()
                (key, value) = part.split(":")
                Storyline.storylineMain[key] = value

    def updateStoryline(story_part:dict):
        return Storyline.storylineMain.update(story_part)

    def toFullStory():
        print(Storyline.storylineMain)

    def toPartStory(part:str):
        print(Storyline.storylineMain[part])