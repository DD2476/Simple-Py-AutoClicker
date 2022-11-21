import pyautogui as pg, os, msvcrt, time, tkinter as tk;from pystyle import Colorate, Colors, Center;from colorama import Fore as ff
class Variables:delay=100;activated=False
class ClickerModules:
    def Click(delay):
        pos = pg.position()
        pg.click(pos[0], pos[1])
        time.sleep(delay/1000)
        return
class UI:
    def StartMenu():
        title = """
 █████╗ ██╗   ██╗████████╗ ██████╗  ██████╗██╗     ██╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝██║     ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║██║   ██║   ██║   ██║   ██║██║     ██║     ██║██║     █████╔╝ █████╗  ██████╔╝
██╔══██║██║   ██║   ██║   ██║   ██║██║     ██║     ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝   ██║   ╚██████╔╝╚██████╗███████╗██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                      
                            [S] - Toggle autoclicker"""
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
    print(Center.XCenter(f"{ff.WHITE}Status: {ff.RED}Off"))
    print(Center.XCenter(f"{ff.WHITE}Delay: {ff.LIGHTCYAN_EX}{Variables.delay}"))
    while True:
        if Variables.activated==True:ClickerModules.Click(Variables.delay)
        if msvcrt.kbhit():
            key = msvcrt.getch()
            val = str(key).removeprefix("b'").removesuffix("'")
            if Variables.activated == True:
                os.system("cls" if os.name == 'nt' else "clear")
                UI.StartMenu()
                print(Center.XCenter(f"{ff.WHITE}Status: {ff.RED}Off"))
                print(Center.XCenter(f"{ff.WHITE}Delay: {ff.LIGHTCYAN_EX}{Variables.delay}"))
            else:
                os.system("cls" if os.name == 'nt' else "clear")
                UI.StartMenu()
                print(Center.XCenter(f"{ff.WHITE}Status: {ff.GREEN}On"))
                print(Center.XCenter(f"{ff.WHITE}Delay: {ff.LIGHTCYAN_EX}{Variables.delay}"))
            if val == "s":
                if Variables.activated == True:
                    Variables.activated = False
                    #print("deactivated")
                else:
                    Variables.activated = True
                    #print("activated")
# CTRL + FORWARD SLASH FOR TOGGLING COMMENTS [CTRL+/]
# def StartGUI():
#     def clickToggleButton():
#         btn_text.set("b")
#         if Variables.activated == True:
#             #button.text = "Deactivate"
#             print("Deactivate")
#             Variables.activated = False
#         else:
#             #button.text = "Activate"
#             print("Activate")
#             Variables.activated = True
#     window = tk.Tk()
#     window.title = "Simple AutoClicker"
#     window.geometry("200x300")
#     window.attributes("-topmost", True)
#     window.resizable(False, False)
#     frame = tk.Frame(window)
#     btn = tk.Button
#     btn_text = tk.StringVar()
#     btn = tk.Button(window, text = 'Toggle', command = clickToggleButton).place(x=10, y=10)
#     btn_text.set("a")
#     btn1 = tk.Button(window, text = 'Exit', command = clickExitButton).place(x=65, y=10)
#     window.mainloop()
#     return
main()