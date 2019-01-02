from tkinter import *
from MainMenu import MainMenu
from Piece import Piece
import constants


class Main:
    def __init__(self, master):
        main_menu = MainMenu(master)
        self.canvas = Canvas(master, width=constants.CANVAS_W, height=constants.CANVAS_H, bg=constants.BACKGROUND)
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
        if event.keysym == "space":
            self.remove_complete_lines()

    def remove_complete_lines(self):
        all_boxes = self.canvas.find_all()
        y_lines = set([self.canvas.coords(box)[3] for box in all_boxes])

        boxes_to_remove = []
        for line in sorted(y_lines):
            boxes_to_remove = self.canvas.find_enclosed(0, line - constants.BLOCK_SIZE - 1, constants.CANVAS_W,
                                                        line + 1)
            if boxes_to_remove.__len__() >= int(constants.CANVAS_W / constants.BLOCK_SIZE):
                for box in boxes_to_remove:
                    print("delete box:", box)
                    self.canvas.delete(box)

        print(boxes_to_remove)


root = Tk()
root.geometry(str(constants.CANVAS_W) + "x" + str(constants.CANVAS_H))
root.configure(bg=constants.BACKGROUND)
root.resizable(False, False)
main = Main(root)
root.update()
main.move_fall()
root.mainloop()
