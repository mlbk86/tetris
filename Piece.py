from random import choice


class Piece:
    SHAPES = (("cyan", (0, 0), (1, 0), (2, 0), (3, 0)),     # I
              ("blue", (0, 0), (1, 0), (2, 0), (2, 1)),     # J
              ("yellow", (0, 0), (1, 0), (1, 0), (1, 1)),   # O
              ("pink", (0, 0), (1, 0), (2, 0), (1, 1)),     # T
              ("orange", (0, 0), (1, 0), (2, 0), (0, 1)),   # L
              ("green", (1, 0), (2, 0), (0, 1), (1, 1)),    # S
              ("red", (0, 0), (1, 0), (1, 1), (2, 1))       # Z
              )
    BLOCK_SIZE = 20

    def __init__(self, canvas):
        self.piece = choice(self.SHAPES)
        self.blocks = []
        self.color = self.piece[0]
        self.canvas = canvas
        self.is_at_bottom = False

        for point in self.piece[1:]:
            block = self.canvas.create_rectangle(
                point[0] * Piece.BLOCK_SIZE + 5,
                point[1] * Piece.BLOCK_SIZE + 5,
                point[0] * Piece.BLOCK_SIZE + Piece.BLOCK_SIZE + 5,
                point[1] * Piece.BLOCK_SIZE + Piece.BLOCK_SIZE + 5,
                fill=self.color
            )
            self.blocks.append(block)

    def move(self, direction):
        if self.can_move_piece(direction):
            x = Piece.get_x(direction)
            y = Piece.get_y(direction)

            for block in self.blocks:
                self.canvas.move(block, x * Piece.BLOCK_SIZE, y * Piece.BLOCK_SIZE)

    def can_move_piece(self, direction):
        for block in self.blocks:
            if not self.can_move_block(block, direction):
                return False

        return True

    def can_move_block(self, block, direction):
        current_coords = self.canvas.coords(block)

        can_move = False

        if direction == "Down":
            if current_coords[3] + self.BLOCK_SIZE <= self.canvas.winfo_height():
                can_move = True
            else:
                self.is_at_bottom = True

        if direction == "Right" and current_coords[2] + self.BLOCK_SIZE <= self.canvas.winfo_width():
            can_move = True

        if direction == "Left" and current_coords[0] - self.BLOCK_SIZE >= 0:
            can_move = True

        return can_move

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

    # def is_at_bottom(self):