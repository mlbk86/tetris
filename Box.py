import constants


def can_move_block(canvas, coords, direction):

    can_move = False
    is_at_bottom = False

    if direction == "Down":
        if coords[3] + constants.BLOCK_SIZE <= canvas.winfo_height():
            can_move = True
        else:
            is_at_bottom = True

    if direction == "Right" and coords[2] + constants.BLOCK_SIZE <= canvas.winfo_width():
        can_move = True

    if direction == "Left" and coords[0] - constants.BLOCK_SIZE >= 0:
        can_move = True

    return can_move, is_at_bottom
