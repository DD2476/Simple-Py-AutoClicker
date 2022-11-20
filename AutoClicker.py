import pyautogui as pg, os, msvcrt;from pystyle import Colorate, Colors, Center;from colorama import Fore as f
class Variables:delay=100;activated=False
class ClickerModules:
    def Click():
        pos = pg.position()
        pg.click(pos[0], pos[1])
        return
class UI:
    def StartMenu():
        title = """
 ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ▄████▄   ██▓     ██▓ ▄████▄   ██ ▄█▀▓█████  ██▀███  
▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▀ ▀█  ▓██▒    ▓██▒▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▒▓█    ▄ ▒██░    ▒██▒▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒▓▓▄ ▄██▒▒██░    ░██░▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
 ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒ ▓███▀ ░░██████▒░██░▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ░▒ ▒  ░░ ▒░▓  ░░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░   ░  ▒   ░ ░ ▒  ░ ▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░          ░ ░    ▒ ░░        ░ ░░ ░    ░     ░░   ░ 
      ░  ░   ░                  ░ ░  ░ ░          ░  ░ ░  ░ ░      ░  ░      ░  ░   ░     
                                     ░                    ░                               """
        print(Colorate.Vertical(Colors.blue_to_purple, Center.XCenter(title)))
        return
def main():
    if os.path.isfile(os.curdir+"\\delay.txt"):
        with open(f"{os.curdir}\\delay.txt", "r") as f:
            try:
                Variables.delay = int(f.read())
            except:
                print(Colorate.Color(Colors.red, Center.XCenter(Center.YCenter("Please type a valid in (in milliseconds) inside delay.txt"))))
                return
    UI.StartMenu()
    while True:
        if Variables.activated==True:ClickerModules.Click()
        if msvcrt.kbhit():
            key = msvcrt.getch()
            val = str(key).removeprefix("b'").removesuffix("'")
            if val == "s":
                if Variables.activated == True:
                    Variables.activated = False
                else:
                    Variables.activated = True
main()