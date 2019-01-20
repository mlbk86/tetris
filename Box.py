"""
Representation of one building block for the tetrominos.

---------------------
author: Michal Blazek
mail: mlbk86@gmail.com
 """

import constants


def can_move_block_direction(canvas, coords, direction, tag):
    can_move = False
    is_at_bottom = False

    if direction == "Down":
        if coords[3] + constants.BLOCK_SIZE <= canvas.winfo_height():

            # find boxes that would be overlapped by current move
            overlapped = canvas.find_overlapping(coords[0] + 1,
                                                 coords[3] + 1,
                                                 coords[2] - 1,
                                                 coords[3] + constants.BLOCK_SIZE - 1)
            can_move = is_box_from_one_piece(overlapped, canvas, tag)

            if not can_move:
                is_at_bottom = True
        else:
            is_at_bottom = True
            can_move = False

    if direction == "Right" and coords[2] + constants.BLOCK_SIZE <= canvas.winfo_width():
        # find boxes that would be overlapped by current move
        overlapped = canvas.find_overlapping(coords[2] + 1,
                                             coords[1] + 1,
                                             coords[2] + constants.BLOCK_SIZE - 1,
                                             coords[3] - 1)
        can_move = is_box_from_one_piece(overlapped, canvas, tag)

    if direction == "Left" and coords[0] - constants.BLOCK_SIZE >= 0:
        # find boxes that would be overlapped by current move
        overlapped = canvas.find_overlapping(coords[0] - constants.BLOCK_SIZE + 1,
                                             coords[1] + 1,
                                             coords[0] - 1,
                                             coords[3] - 1)
        can_move = is_box_from_one_piece(overlapped, canvas, tag)

    return can_move, is_at_bottom


# Check if block can move to new coords without overlapping another piece
def can_move_block_coords(canvas, coords, tag):
    # find boxes that would be overlapped by current move
    overlapped = canvas.find_overlapping(coords[0] + 1,
                                         coords[3] + 1,
                                         coords[2] - 1,
                                         coords[3] + constants.BLOCK_SIZE - 1)
    return is_box_from_one_piece(overlapped, canvas, tag)


# check if (new) potential coordinates are within the canvas dimensions
def coords_are_valid(x1, y1, x2, y2):
    return 0 <= x1 <= constants.CANVAS_W \
           and 0 <= x2 <= constants.CANVAS_W \
           and 0 <= y1 <= constants.CANVAS_H \
           and 0 <= y2 <= constants.CANVAS_H


# check if current box belongs to the same piece as the one that would be overwritten by its move
# returns can_move and is_at_bottom
def is_box_from_one_piece(overlapped, canvas, tag):
    if overlapped:
        for box in overlapped:
            box_tags = canvas.gettags(box)
            if str(tag) in box_tags:
                return True
        can_move = False
    else:
        can_move = True

    return can_move
