#!/usr/bin/env python

"""
Simple tetris game

---------------------
author: Michal Blazek
mail: mlbk86@gmail.com
 """


from tkinter import *
from tkinter import messagebox
from Piece import Piece
import constants
from TextAndValue import TextAndValue


class Main:
    def __init__(self, master):
        self.canvas = Canvas(master, width=constants.CANVAS_W, height=constants.CANVAS_H, bg=constants.BACKGROUND)
        self.canvas.grid(column=0, row=0, rowspan=5, sticky=(N, W, E, S))
        self.current_piece = None
        self.master = master
        self.master.bind("<Key>", self.handle_move)
        self.is_new_game = True
        self.is_game_over = True
        self.speed = constants.INITIAL_SPEED

        self.score_frame = TextAndValue(master, label="Score", value=0)
        self.score_frame.grid(column=1, row=0, sticky=(N, W, E), pady=3)

        self.level_frame = TextAndValue(master, label="Level", value=1)
        self.level_frame.grid(column=1, row=1, sticky=(N, W, E), pady=3)

        self.direction_label = Label(master, text="Rotate: arrow UP", bg="grey", font=("Arial", 12))
        self.direction_label.grid(column=1, row=2, sticky=(N, W, E), pady=10)
        self.new_game_button = Button(master, text='New game', command=self.start, background="grey", fg="blue",
                                      highlightbackground=constants.BACKGROUND)
        self.new_game_button.grid(column=1, row=3, sticky=(N, W, E), pady=10)
        self.master.grid_rowconfigure(3, weight=1)

    def start(self):
        self.canvas.delete(ALL)
        self.is_new_game = True
        self.current_piece = None
        self.is_game_over = False
        self.score_frame.set(0)
        self.level_frame.set(1)
        self.speed = constants.INITIAL_SPEED

    # adds new piece to the board
    def add_piece(self):
        self.current_piece = Piece(canvas=self.canvas)

    # main loop for moving, adding and removing lines
    def move_fall(self):
        if not self.is_game_over:
            if self.is_new_game:
                self.add_piece()
                self.is_new_game = False

            self.current_piece.move("Down")

            if self.current_piece.is_at_bottom:
                self.remove_complete_lines()

                if self.current_piece.is_at_top:
                    messagebox.showinfo("GAME OVER", "Game over! Your score: " + str(self.score_frame.get()))
                    self.is_game_over = True

                if not self.is_game_over:
                    self.add_piece()

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
                self.score_frame.set(self.score_frame.get() + 1)
                if self.score_frame.get() % 10 == 0:
                    self.level_frame.set(self.level_frame.get() + 1)
                    if self.speed > constants.SPEED_STEP:
                        self.speed -= constants.SPEED_STEP

                # fall boxes that are above removed line
                above_boxes = self.canvas.find_overlapping(1, 1, constants.CANVAS_W - 1, line - 1)
                if above_boxes:
                    for box in above_boxes:
                        self.canvas.move(box, 0, constants.BLOCK_SIZE)


root = Tk()
root.geometry(str(constants.CANVAS_W+110) + "x" + str(constants.CANVAS_H))
root.configure(bg=constants.BACKGROUND)
root.resizable(False, False)
main = Main(root)
root.update()
main.move_fall()
root.mainloop()
