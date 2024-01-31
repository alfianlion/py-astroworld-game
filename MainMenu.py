class MainMenu:
    def welcomeMessage(gamemenu : dict):
        print('Welcome to AstroWorld!\n')
        for key, value in gamemenu.items():
            print(key + ")" + value)

    def menuOption():
        return print('========= MAIN MENU =========')