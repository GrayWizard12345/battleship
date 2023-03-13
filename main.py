from player import Player

MAIN_MENU = {"1. New Game": 1, "2. Quite": 2}
NEW_GAME_MENU = {"1. PVP": 3, "2. PVE": 4}


PLAYER1_BOARD = [["*" for i in range(10)] for j in range(10)]
PLAYER2_BOARD = [["*" for i in range(10)] for j in range(10)]

player1 = Player(PLAYER1_BOARD)
player2 = Player(PLAYER2_BOARD)

X_AXIS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Y_AXIS = "A,B,C,D,E,F,G,H,I,J".split(sep=",")


def draw_board(board):
    print("    ", end="")
    for i in X_AXIS:
        print(i, end="   ")
    print()
    for i, row in enumerate(board):
        print(Y_AXIS[i], end=" ")
        for cell in row:
            print("| " + str(cell) + " ", end="")
        print()


def insert_ship(player: Player, coord1, coord2):
    """
    Inserts the ship that starts at coord1 and ends at coord2 into the board
    If coordinates are invalid returns false.
    If valid, inserts the ship and returns True

    :param player: an object of type Player that has a board and ships
    :param coord1: A string of length 2
    :param coord2: A string of length 2
    :return: a bool value
    """
    board = player.board
    x1, y1 = get_coordinates_ascii(coord1)
    x2, y2 = get_coordinates_ascii(coord2)

    if x1 != x2 and y1 != y2:
        return False

    if 0 <= x1 < 10 and 0 <= y1 < 10 and 0 <= x2 < 10 and 0 <= y2 < 10:
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1, y2 + 1):
                if board[i][x1] == 1:
                    return False
                board[i][x1] = 1
        else:
            if x1 > x2:
                x1, x2 = x2, x1
            for i in range(x1, x2 + 1):
                if board[y1][i] == 1:
                    return False
                board[y1][i] = 1
    
    player.ships.append([(x1, y1), (x2, y2)])  # memorise ships
    return True


def get_coordinates_ascii(coord):
    y, x = list(coord)
    x = int(x)
    y = ord(y) - ord("A")  # converts symbol coord to ascii value (from 0 - 9)
    return x, y


def show_main_menu():
    """
    Показывает на экране главное меню
    """

    for menu_item in MAIN_MENU:
        print(menu_item)


if __name__ == '__main__':
    draw_board(PLAYER2_BOARD)
    insert_ship(PLAYER2_BOARD, "A0", "F0")
    insert_ship(PLAYER2_BOARD, "C3", "C1")
    draw_board(PLAYER2_BOARD)