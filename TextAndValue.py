"""
This class is used to show label and value

---------------------
author: Michal Blazek
mail: mlbk86@gmail.com
"""

from tkinter import *


class TextAndValue(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg="grey")
        label = ""
        if kwargs["label"]:
            label = kwargs["label"]

        value = 0

        if kwargs["value"]:
            value = kwargs["value"]

        self.score_label = Label(self, text=label + ": ", font=("Arial", 16), bg="grey")
        self.score_label.pack(fill=BOTH, side="left")
        # self.score_label.grid(column=0, row=0, sticky=(N, W, E), pady=3)
        self.score_val = value
        self.score_val_str = StringVar()
        self.score_val_str.set(str(self.score_val))
        self.score = Label(self, textvariable=self.score_val_str, font=("Arial", 16), bg="grey")
        self.score.pack(fill=BOTH, side="left")

        # self.score.grid(column=1, row=0, sticky=(N, W, E), pady=3)

    def set(self, value):
        self.score_val = value
        self.score_val_str.set(str(self.score_val))

    def get(self):
        return int(self.score_val_str.get())
