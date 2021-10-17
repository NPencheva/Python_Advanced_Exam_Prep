from io import StringIO
import sys

input1 = """Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 3)"""
input2 = """George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)"""
input_test = """Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(0, 1)
(-1, 5)
(-2, 7)
(3, 3)"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input_test)

# n, m = [int(x) for x in input().split()]
size = 7


def read_matrix():
    this_matrix = []

    for _ in range(size):
        row = [x for x in input().split(" ")]
        this_matrix.append(row)

    return this_matrix


def check_is_in_dartboard():
    if coord_row < 0 or coord_col < 0 or coord_row >= size or coord_col >= size:
        return False
    else:
        return True


def check_if_is_number():
    if coord_row == 0 or coord_row == size - 1 or coord_col == 0 or coord_col == size - 1:
        return True
    else:
        return False


def check_if_is_d():
    if point_hit == "D":
        return True


def calculate_d():
    points_scored = (int(matrix[coord_row][0]) + int(matrix[coord_row][size - 1]) + int(matrix[0][coord_col]) + int(
        matrix[size - 1][coord_col])) * 2
    return points_scored


def check_if_is_t():
    if point_hit == "T":
        return True


def calculate_t():
    points_scored = (int(matrix[coord_row][0]) + int(matrix[coord_row][size - 1]) + int(matrix[0][coord_col]) + int(
        matrix[size - 1][coord_col])) * 3
    return points_scored


player_1, player_2 = input().split(", ")
matrix = read_matrix()

player_1_score = 501
player_2_score = 501
turn_counter = 1
player_1_turn_counter = 0
player_2_turn_counter = 0

player_1_turn = False
player_2_turn = False
is_winner = False


while not is_winner:
    coord_row, coord_col = [int(el) for el in input().strip("()").split(", ")]

    if turn_counter % 2 != 0:
        player_1_turn = True
        player_2_turn = False
        player_1_turn_counter += 1
    else:
        player_2_turn = True
        player_1_turn = False
        player_2_turn_counter += 1
    turn_counter += 1

    if not check_is_in_dartboard():
        continue
    point_hit = matrix[coord_row][coord_col]

    if point_hit == "B":
        is_winner = True
        if player_1_turn:
            print(f"{player_1} won the game with {player_1_turn_counter} throws!")
        else:
            print(f"{player_2} won the game with {player_2_turn_counter} throws!")
        break

    elif check_if_is_number():
        if player_1_turn:
            player_1_score -= int(point_hit)
        else:
            player_2_score -= int(point_hit)
    elif check_if_is_d():
        if player_1_turn:
            player_1_score -= calculate_d()
        else:
            player_2_score -= calculate_d()
    elif check_if_is_t():
        if player_1_turn:
            player_1_score -= calculate_t()
        else:
            player_2_score -= calculate_t()

    if player_1_score <= 0:
        is_winner = True
        print(f"{player_1} won the game with {player_1_turn_counter} throws!")
        break
    elif player_2_score <= 0:
        is_winner = True
        print(f"{player_2} won the game with {player_2_turn_counter} throws!")
        break











