from player import Player
from utils import get_coordinates_ascii, check_if_coord_is_valid, get_coord, calculate_length

MAIN_MENU = {"1. New Game": 1, "2. Quit": 2}

NEW_GAME_MENU = {"1. PVP": 3, "2. PVE": 4}


PLAYER1_BOARD = [["*" for i in range(10)] for j in range(10)]
PLAYER2_BOARD = [["*" for i in range(10)] for j in range(10)]

player1 = Player(PLAYER1_BOARD)
player2 = Player(PLAYER2_BOARD)

X_AXIS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Y_AXIS = "A,B,C,D,E,F,G,H,I,J".split(sep=",")


def draw_board(board, hide=False):
    print("    ", end="")
    for i in X_AXIS:
        print(i, end="   ")
    print()
    for i, row in enumerate(board):
        print(Y_AXIS[i], end=" ")
        for cell in row:
            cell_content = str(cell)
            if cell_content == '1' and hide:
                cell_content = '*'
            print("| " + cell_content + " ", end="")
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

def menu_loop():
    """
    Показывает на экране главное меню
    """
    action = exit
    while True:
        for menu_item in MAIN_MENU:
            print(menu_item)
        try:
            choice = int(input())
            if choice in MAIN_MENU.values():
                action = MENU_ACTIONS[choice]
                break
        except:
            print("Неверный формат ввода. Введите только число.")
    action()


POSSIBLE_SHIP_SIZES = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

def game_loop():

    # Insert ships of 1
    print("Игрок 1 вводит коробли")
    insert_all_ships_for_player(player1)

    # Insert ships of 2
    print("Игрок 2 вводит коробли")
    insert_all_ships_for_player(player2)

    # Start shooting alternating
    player_1_shooting = True

    while True:
        if player_1_shooting:
            print("Стреляет игрок 1")
            draw_board(player2.board, True)
            coord = get_coord("Введите координаы выстрела:")
            result = player2.got_shot(coord)
            if len(result) == 1:
                print("Вы попытались выстрелить куда уже стреляли ранее. Попробуйте еще раз!")
            else:
                if result[0]:
                    if result[1]:
                        print("Один из короблей противника утонул!")
                        if player2.check_if_all_ships_sunken():
                            print("Победил игрок 1!")
                            break
                    print("Вы попали по короблю! Опять ваш ход!")
                else:
                    player_1_shooting = not player_1_shooting
        else:
            print("Стреляет игрок 2")
            draw_board(player1.board, True)
            coord = get_coord("Введите координаы выстрела:")
            result = player1.got_shot(coord)
            if len(result) == 1:
                print("Вы попытались выстрелить куда уже стреляли ранее. Попробуйте еще раз!")
            else:
                if result[0]:
                    if result[1]:
                        print("Один из короблей противника утонул!")
                        if player1.check_if_all_ships_sunken():
                            print("Победил игрок 2!")
                            break
                    print("Вы попали по короблю! Опять ваш ход!")
                else:
                    player_1_shooting = not player_1_shooting

MENU_ACTIONS = [0, game_loop, exit]

def insert_all_ships_for_player(player):
    for ship_size in POSSIBLE_SHIP_SIZES:
        while True:
            print(f"Вы вводите корабль длинной {ship_size}")
            coord1 = get_coord("Введите координаты начала коробля:")
            coord2 = get_coord("Введите координаты конца коробля:")
            length = calculate_length(coord1, coord2)
            if length != ship_size:
                print(f"Длинна коробля не равна {ship_size}\nПопробуйте заного!")
                continue
            success = insert_ship(player, coord1, coord2)
            if success:
                draw_board(player.board)
                break
            else:
                print("В эти координаты корабль нельзя вставлять!")


if __name__ == '__main__':
    menu_loop()
