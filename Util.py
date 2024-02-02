class Util:
     isLauncherRunning = False
     system = any
     os = ''

     def clearTerminal(os):
        if os == 'cls':
            _ = Util.system('cls')
        else:
            _ = Util.system('clear')