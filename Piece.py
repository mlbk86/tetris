from random import choice
import constants
import Box


class Piece:
    SHAPES = (("cyan", (0, 0), (1, 0), (2, 0), (3, 0)),  # I
              # ("blue", (0, 0), (1, 0), (2, 0), (2, 1)),     # J
              # ("yellow", (0, 0), (1, 0), (1, 1)),           # O
              ("pink", (0, 0), (1, 0), (2, 0), (1, 1)),  # T
              # ("orange", (0, 0), (1, 0), (2, 0), (0, 1)),   # L
              # ("green", (1, 0), (2, 0), (0, 1), (1, 1)),    # S
              # ("red", (0, 0), (1, 0), (1, 1), (2, 1))       # Z
              )

    def __init__(self, canvas):
        self.piece = choice(self.SHAPES)
        self.boxes = []
        self.color = self.piece[0]
        self.canvas = canvas
        self.is_at_bottom = False

        for point in self.piece[1:]:
            block = self.canvas.create_rectangle(
                point[0] * constants.BLOCK_SIZE + 5,
                point[1] * constants.BLOCK_SIZE + 5,
                point[0] * constants.BLOCK_SIZE + constants.BLOCK_SIZE + 5,
                point[1] * constants.BLOCK_SIZE + constants.BLOCK_SIZE + 5,
                fill=self.color
            )
            self.boxes.append(block)

    def move(self, direction):
        if self.can_move_piece(direction):
            x = Piece.get_x(direction)
            y = Piece.get_y(direction)

            for box in self.boxes:
                self.canvas.move(box, x * constants.BLOCK_SIZE, y * constants.BLOCK_SIZE)

    def can_move_piece(self, direction):
        for box in self.boxes:
            result, self.is_at_bottom = Box.can_move_block(self.canvas, self.canvas.coords(box), direction)
            if not result:
                return False

        return True

    @staticmethod
    def get_x(direction):

        return {
            "Down": 0,
            "Right": 1,
            "Left": -1
        }[direction]

    @staticmethod
    def get_y(direction):

        return {
            "Down": 1,
            "Right": 0,
            "Left": 0
        }[direction]
