class MainMenu:
    def welcomeMessage(gamemenu : dict):
        print('Welcome to AstroWorld!\n')
        for key, value in gamemenu.items():
            print(key + ")" + value)