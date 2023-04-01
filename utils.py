from math import sqrt


def get_coordinates_ascii(coord):
    """
    :param coord: a string of len 2. (example, A0, F8)
    :return: numeric coordinate (example 0 0, 6 8)
    """
    y, x = list(coord)
    x = int(x)
    y = ord(y) - ord("A")  # converts symbol coord to ascii value (from 0 - 9)
    return x, y


def check_if_coord_is_valid(coord):
    if len(coord) != 2: return False

    if 'A' > coord[0] or coord[0] > 'J':
        return False

    if '0' > coord[1] or coord[1] > '9':
        return False

    return True


def get_coord(message):
    while True:
        coord = input(message)
        if check_if_coord_is_valid(coord):
            return coord
        else:
            print("Недопустимая координата!")


def calculate_length(coord1, coord2):
    x1, y1 = get_coordinates_ascii(coord1)
    x2, y2 = get_coordinates_ascii(coord2)

    if x1 != x2 and y1 != y2:
        return -1

    if x1 == x2:
        length = abs(y1 - y2)  # abs(3 - 5) = 2

    if y1 == y2:
        length = abs(x1 - x2)  # abs(3 - 5) = 2

    length += 1

    return length
