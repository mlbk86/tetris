from tkinter import *


class MainMenu:
    def __init__(self, master):
        main_menu = Menu(master)
        master.config(menu=main_menu)
        submenu_file = Menu(main_menu)
        main_menu.add_cascade(label="Game", menu=submenu_file)
        submenu_file.add_command(label="New game", command=MainMenu.do_nothing)

    @staticmethod
    def do_nothing():
        print("do nothing for now")
