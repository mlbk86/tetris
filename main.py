from tkinter import *
from MainMenu import MainMenu
from Piece import Piece


class Main:
    def __init__(self, master):
        main_menu = MainMenu(master)
        self.canvas = Canvas(master, width=300, height=600)
        self.canvas.grid(row=0, pady=100)
        self.canvas.pack()
        self.current_piece = None
        self.xMove = 0
        self.yMove = 1
        self.master = master

    def add_piece(self):
        self.current_piece = Piece(canvas=self.canvas)

    def move_down(self):
        if self.current_piece.can_move_piece():
            self.current_piece.move(self.xMove, self.yMove)
            self.master.after(500, self.move_down)


root = Tk()
main = Main(root)
main.add_piece()
root.update()
main.move_down()
root.mainloop()



