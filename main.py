from tkinter import *
from tkinter import messagebox
from tkinter import font

from MainMenu import MainMenu
from Piece import Piece
import constants


class Main:
    def __init__(self, master):
        main_menu = MainMenu(master)
        self.canvas = Canvas(master, width=constants.CANVAS_W, height=constants.CANVAS_H, bg=constants.BACKGROUND)
        self.canvas.grid(column=0, row=0, rowspan=2, sticky=(N, W, E, S))
        self.current_piece = None
        self.master = master
        self.master.bind("<Key>", self.handle_move)
        self.is_new_game = True
        self.is_game_over = False
        self.score_frame = Frame(master, borderwidth=3)
        self.score_frame.grid(column=1, row=0, sticky=(N, W, E))
        self.score_label = Label(self.score_frame, text='Score: ', font=('Arial', 16))
        self.score_val = 0
        self.score_val_str = StringVar()
        self.score_val_str.set(str(self.score_val))
        self.score = Label(self.score_frame, textvariable=self.score_val_str, font=('Arial', 16))
        self.score_label.pack(side='left')
        self.score.pack(side='left')
        self.level_frame = Frame(master, borderwidth=3)
        self.level_frame.grid(column=1, row=1, sticky=(N, W, E))
        self.level_label = Label(self.level_frame, text='Level: ', font=('Arial', 16))
        self.level_val = 1
        self.level_val_str = StringVar()
        self.level_val_str.set(str(self.level_val))
        self.level = Label(self.level_frame, textvariable=self.level_val_str, font=('Arial', 16))
        self.level_label.pack(side='left')
        self.level.pack(side='left')
        self.master.grid_rowconfigure(1, weight=1)
        self.speed = 500

    def start(self):
        self.canvas.delete(ALL)
        self.is_new_game = True
        self.current_piece = None
        self.is_game_over = False
        self.score_val = 0
        self.level_val = 1
        self.master.after(self.speed, self.move_fall)

    # adds new piece to the board
    def add_piece(self):
        self.current_piece = Piece(canvas=self.canvas)

    # main loop for moving, adding and removing lines
    def move_fall(self):
        if self.is_new_game:
            self.add_piece()
            self.is_new_game = False

        self.current_piece.move("Down")

        if self.current_piece.is_at_bottom:
            self.remove_complete_lines()

            if self.current_piece.is_at_top:
                messagebox.showinfo("GAME OVER", "Game over :-(")
                self.is_game_over = True
                self.start()
                return

            self.add_piece()

        if not self.is_game_over:
            self.master.after(self.speed, self.move_fall)

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
        if event.keysym == "Up":
            self.current_piece.rotate()

    def remove_complete_lines(self):
        all_boxes = self.canvas.find_all()
        y_lines = set([self.canvas.coords(box)[3] for box in all_boxes])

        for line in sorted(y_lines):
            boxes_to_remove = self.canvas.find_enclosed(0, line - constants.BLOCK_SIZE - 1, constants.CANVAS_W,
                                                        line + 1)
            if boxes_to_remove.__len__() >= int(constants.CANVAS_W / constants.BLOCK_SIZE):
                for box in boxes_to_remove:
                    self.canvas.delete(box)
                self.score_val += 1
                self.score_val_str.set(str(self.score_val))
                if self.score_val % 10 == 0:
                    self.level_val += 1
                    if self.speed > 50:
                        self.speed -= 50

                # fall boxes that are above removed line
                above_boxes = self.canvas.find_overlapping(1, 1, constants.CANVAS_W - 1, line - 1)
                if above_boxes:
                    for box in above_boxes:
                        self.canvas.move(box, 0, constants.BLOCK_SIZE)


root = Tk()
root.geometry(str(constants.CANVAS_W+100) + "x" + str(constants.CANVAS_H))
root.configure(bg=constants.BACKGROUND)
root.resizable(False, False)
main = Main(root)
root.update()
main.move_fall()
root.mainloop()
