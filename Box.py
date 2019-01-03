import constants


def can_move_block(canvas, coords, direction, tag):
    can_move = False
    is_at_bottom = False

    if direction == "Down":
        if coords[3] + constants.BLOCK_SIZE <= canvas.winfo_height():
            overlapped = canvas.find_overlapping(coords[0] + 1,
                                                 coords[3] + 1,
                                                 coords[2] - 1,
                                                 coords[3] + constants.BLOCK_SIZE - 1)
            if overlapped:
                for box in overlapped:
                    box_tags = canvas.gettags(box)
                    if str(tag) in box_tags:
                        return True, False
                can_move = False
                is_at_bottom = True
            else:
                can_move = True
        else:
            is_at_bottom = True

    if direction == "Right" and coords[2] + constants.BLOCK_SIZE <= canvas.winfo_width():
        overlapped = canvas.find_overlapping(coords[2] + 1,
                                             coords[1] + 1,
                                             coords[2] + constants.BLOCK_SIZE - 1,
                                             coords[3] - 1)
        if overlapped:
            for box in overlapped:
                box_tags = canvas.gettags(box)
                if str(tag) in box_tags:
                    return True, False
            can_move = False
        else:
            can_move = True

    if direction == "Left" and coords[0] - constants.BLOCK_SIZE >= 0:
        overlapped = canvas.find_overlapping(coords[0] - constants.BLOCK_SIZE + 1,
                                             coords[1] + 1,
                                             coords[0] - 1,
                                             coords[3] - 1)
        if overlapped:
            for box in overlapped:
                box_tags = canvas.gettags(box)
                if str(tag) in box_tags:
                    return True, False
            can_move = False
        else:
            can_move = True

    return can_move, is_at_bottom
