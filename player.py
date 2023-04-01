from utils import get_coordinates_ascii


class Player:

    def __init__(self, board):
        self.board = board
        self.ships = []
        self.sunken_ships = 0

    def got_shot(self, shoot_coord):
        x, y = get_coordinates_ascii(shoot_coord)
        is_hit = False
        is_sunken = False

        for ship_start, ship_end in self.ships:
            if self.board[y][x] not in ('*', 1):
                return [False]  # Return only one value if you cannot shoot here.
            if ship_start[0] <= x <= ship_end[0] and ship_start[1] <= y <= ship_end[1]:
                self.board[y][x] = 'x'
                is_hit = True
                is_sunken = self.check_if_sunken(ship_start, ship_end)
                if is_sunken: self.sunken_ships += 1
                return is_hit, is_sunken

        self.board[y][x] = '0'

        return is_hit, is_sunken

    def check_if_sunken(self, ship_start, ship_end):
        for x in range(ship_start[0], ship_end[0] + 1):
            for y in range(ship_start[1], ship_end[1] + 1):
                if self.board[y][x] != 'x':
                    return False

        return True

    def check_if_all_ships_sunken(self):
        return len(self.ships) == self.sunken_ships
