from random import choice, getrandbits
import constants
import Box


class Piece:
    SHAPES = (("cyan", (0, 0), (1, 0), (2, 0), (3, 0)),  # I
              ("blue", (0, 0), (1, 0), (2, 0), (2, 1)),  # J
              ("yellow", (0, 0), (1, 0), (1, 1)),  # O
              ("pink", (0, 0), (1, 0), (2, 0), (1, 1)),  # T
              ("orange", (0, 0), (1, 0), (2, 0), (0, 1)),  # L
              ("green", (1, 0), (2, 0), (0, 1), (1, 1)),  # S
              ("red", (0, 0), (1, 0), (1, 1), (2, 1))  # Z
              )

    def __init__(self, canvas):
        self.piece = choice(self.SHAPES)
        self.boxes = []
        self.color = self.piece[0]
        self.canvas = canvas
        self.is_at_bottom = False
        self.is_at_top = False
        self.direction = 0

        # hash tag is used to recognize boxes grouped into one piece
        self.hash_tag = getrandbits(64)

        for point in self.piece[1:]:
            box = self.canvas.create_rectangle(
                point[0] * constants.BLOCK_SIZE + 5,
                point[1] * constants.BLOCK_SIZE + 5,
                point[0] * constants.BLOCK_SIZE + constants.BLOCK_SIZE + 5,
                point[1] * constants.BLOCK_SIZE + constants.BLOCK_SIZE + 5,
                fill=self.color,
                tags=self.hash_tag
            )
            self.boxes.append(box)

    def move(self, direction):
        if self.can_move_piece(direction):
            x = Piece.get_x(direction)
            y = Piece.get_y(direction)

            for box in self.boxes:
                self.canvas.move(box, x * constants.BLOCK_SIZE, y * constants.BLOCK_SIZE)
        elif self.is_at_bottom:
            for box in self.boxes:
                self.canvas.itemconfig(box, tags=())
                if self.canvas.coords(box)[1] <= 5:
                    self.is_at_top = True

    def can_move_piece(self, direction):
        for box in self.boxes:
            result, self.is_at_bottom = Box.can_move_block(self.canvas, self.canvas.coords(box), direction,
                                                           self.hash_tag)
            if not result:
                return False

        return True

    def rotate(self):
        color = {
            "cyan": self.rotate_cyan,
            "blue": self.rotate_blue
        }

        color[self.color]()

    def rotate_cyan(self):
        new_coords = []

        root_x = self.canvas.coords(self.boxes[1])[0]
        root_y = self.canvas.coords(self.boxes[1])[1]

        if self.direction == 0:
            for i in range(-1, 3):
                y = root_y + (i * constants.BLOCK_SIZE)
                new_coords.append((root_x, y, root_x + constants.BLOCK_SIZE, y + constants.BLOCK_SIZE))
            self.direction = 1
        else:
            for i in range(-1, 3):
                x = root_x + (i * constants.BLOCK_SIZE)
                new_coords.append((x, root_y, x + constants.BLOCK_SIZE, root_y + constants.BLOCK_SIZE))
            self.direction = 0

        for coord in new_coords:
            if not (Box.coords_are_valid(coord[0], coord[1], coord[2], coord[3])):
                return

        self.redraw(new_coords)

    def rotate_blue(self):
        print("BLUE")

    def redraw(self, new_coords):
        for box in self.boxes:
            self.canvas.delete(box)

        self.boxes.clear()

        for point in new_coords:
            box = self.canvas.create_rectangle(
                point[0],
                point[1],
                point[0] + constants.BLOCK_SIZE,
                point[1] + constants.BLOCK_SIZE,
                fill=self.color,
                tags=self.hash_tag
            )
            self.boxes.append(box)

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
