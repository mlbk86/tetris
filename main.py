from tkinter import *
from MainMenu import MainMenu
from Piece import Piece


class Main:
    def __init__(self, master):
        main_menu = MainMenu(master)
        self.canvas = Canvas(master, width=250, height=560)
        self.canvas.grid(column=0, row=0, sticky=(N, W, E, S))
        self.canvas.pack()
        self.current_piece = None
        self.xMove = 0
        self.yMove = 1
        self.master = master
        self.master.bind("<Key>", self.handle_move)
        self.is_new_game = True
        self.pieces = []

    def add_piece(self):
        self.current_piece = Piece(canvas=self.canvas)
        self.pieces.append(self.current_piece)

    def move_fall(self):
        if self.is_new_game:
            self.add_piece()
            self.is_new_game = False

        if self.current_piece.is_at_bottom:
            self.add_piece()

        self.current_piece.move("Down")
        self.master.after(500, self.move_fall)

    def move(self, direction):
        self.current_piece.move(direction)

    # handle key presses
    def handle_move(self, event):
        if event.keysym == "Left":
            self.move("Left")
        if event.keysym == "Right":
            self.move("Right")
        if event.keysym == "Down":
            self.move("Down")


root = Tk()
root.geometry("250x560")
main = Main(root)
root.update()
main.move_fall()
root.mainloop()
