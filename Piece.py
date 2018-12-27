from random import choice

class Piece:
    SHAPES = (("cyan", (0, 0), (1, 0), (2, 0), (3, 0)),  # I
              ("blue", (0, 0), (1, 0), (2, 0), (2, 1))   # J
              )
    BLOCK_SIZE = 20

    def __init__(self, canvas):
        self.piece = choice(self.SHAPES)
        self.blocks = []
        self.color = self.piece[0]
        self.canvas = canvas

        for point in self.piece[1:]:
            block = self.canvas.create_rectangle(
                point[0] * Piece.BLOCK_SIZE + 5,
                point[1] * Piece.BLOCK_SIZE + 5,
                point[0] * Piece.BLOCK_SIZE + Piece.BLOCK_SIZE + 5,
                point[1] * Piece.BLOCK_SIZE + Piece.BLOCK_SIZE + 5,
                fill=self.color
            )
            self.blocks.append(block)

    def move(self, x, y):
        for block in self.blocks:
            self.canvas.move(block, x * Piece.BLOCK_SIZE, y * Piece.BLOCK_SIZE)

    def can_move_piece(self):
        for block in self.blocks:
            if not self.can_move_block(block):
                return False

        return True

    def can_move_block(self, block):
        current_coords = self.canvas.coords(block)

        if current_coords[3] + self.BLOCK_SIZE > self.canvas.winfo_height():
            return False;

        return True
