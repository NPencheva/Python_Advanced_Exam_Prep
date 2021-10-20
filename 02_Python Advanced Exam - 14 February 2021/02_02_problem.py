from io import StringIO
import sys
from math import floor

input1 = """5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
right
right
up
up
left
down"""
input2 = """8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
left"""
input_test = """5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
yeah
left
up
right
left
left
down"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input_test)

# n, m = [int(x) for x in input().split()]
size = int(input())


def read_matrix():
    this_matrix = []

    for _ in range(size):
        row_ = [x for x in input().split(" ")]
        this_matrix.append(row_)

    return this_matrix


def check_is_in_field(r, c):
    if r < 0 or c < 0 or r >= size or c >= size:
        return False
    else:
        return True


def player_position():
    r, c = 0, 0
    is_my_position = False

    for row_index in range(size):
        for col_index in range(size):
            if matrix[row_index][col_index] == "P":
                r, c = row_index, col_index
                is_my_position = True
                break
        if is_my_position:
            break

    return r, c


def direction_movement(comm, curr_row, curr_col):
    if comm == "up":
        curr_row -= 1
    elif comm == "down":
        curr_row += 1
    elif comm == "left":
        curr_col -= 1
    elif comm == "right":
        curr_col += 1

    return curr_row, curr_col


matrix = read_matrix()
coins_collected = 0
valid_commands = ("up", "down", "left", "right")
row, col = player_position()
current_row, current_col = row, col
path = []
is_winner = False

while True:
    command = input()
    if command not in valid_commands:
        continue
    else:
        current_row, current_col = direction_movement(command, current_row, current_col)
        if not check_is_in_field(current_row, current_col):
            break
        point_hit = matrix[current_row][current_col]
        if point_hit == "X":
            break
        else:
            path.append([current_row, current_col])
            if point_hit != "P":
                coins_collected += int(point_hit)

        if coins_collected >= 100:
            is_winner = True
            break


if is_winner:
    print(f"You won! You've collected {coins_collected} coins.")
else:
    coins_collected = floor(coins_collected * 0.5)
    print(f"Game over! You've collected {coins_collected} coins.")
print("Your path:")

for el in path:
    print(el)
