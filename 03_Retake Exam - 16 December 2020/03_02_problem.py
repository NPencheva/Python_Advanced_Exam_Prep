from io import StringIO
import sys

input1 = """Hello
4
P---
Mark
-l-y
--e-
4
down
right
right
right"""
input2 = """Initial
5
-----
t-r--
--Pa-
--S--
z--t-
4
up
left
left
left"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)


# n, m = [int(x) for x in input().split()]


def read_matrix():
    this_matrix = []

    for _ in range(size):
        row_ = [x for x in input()]
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


def check_if_is_letter():
    if point_hit != "-":
        return True


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


initial_string = input()
size = int(input())
matrix = read_matrix()
number_of_commands = int(input())

# row, col = player_position()
# current_row, current_col = row, col
current_row, current_col = player_position()

for turn in range(number_of_commands):
    command = input()
    matrix[current_row][current_col] = "-"
    new_row, new_col = direction_movement(command, current_row, current_col)
    if not check_is_in_field(new_row, new_col):
        if initial_string:
            initial_string = initial_string[:-1]
    else:
        current_row, current_col = direction_movement(command, current_row, current_col)
    point_hit = matrix[current_row][current_col]
    if check_if_is_letter():
        initial_string += point_hit
    matrix[current_row][current_col] = "P"

print(initial_string)

for row in range(len(matrix)):
    print("".join(matrix[row]))
