from io import StringIO
import sys

input1 = """. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . ."""
input2 = """. . . . . . . .
. . . Q . . . .
. . . . . . . .
. . . . . . . .
Q . . . Q . . .
. . K . . . . .
. . . . . . Q .
. . . Q . . . ."""
input_test = """ K . . . . . . .
Q . . . . . . .
. . Q . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . Q Q .
. Q . Q . . . ."""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input_test)

# n, m = [int(x) for x in input().split()]
size = 8


def read_matrix():
    this_matrix = []

    for _ in range(size):
        row_ = [x for x in input().split(" ")]
        this_matrix.append(row_)

    return this_matrix


def king_position():
    r, c = 0, 0
    is_king_position = False

    for row_index in range(size):
        for col_index in range(size):
            if matrix[row_index][col_index] == "K":
                r, c = row_index, col_index
                is_king_position = True
                break
        if is_king_position:
            break

    return r, c


def move_up():
    r, c = king_position()
    result = []
    for row_index in range(r - 1, -1, -1):
        curr_position = matrix[row_index][c]
        if curr_position == ".":
            continue
        elif curr_position == "Q":
            result = [row_index, c]
            break

    if result:
        return result


def move_down():
    r, c = king_position()
    result = []
    for row_index in range(r + 1, size):
        curr_position = matrix[row_index][c]
        if curr_position == ".":
            continue
        elif curr_position == "Q":
            result = [row_index, c]
            break

    if result:
        return result


def move_left():
    r, c = king_position()
    result = []
    for col_index in range(c - 1, -1, - 1):
        curr_position = matrix[r][col_index]
        if curr_position == ".":
            continue
        elif curr_position == "Q":
            result = [r, col_index]
            break

    if result:
        return result


def move_right():
    r, c = king_position()
    result = []
    for col_index in range(c + 1, size):
        curr_position = matrix[r][col_index]
        if curr_position == ".":
            if col_index < size - 1:
                col_index += 1
                continue
            else:
                break
        elif curr_position == "Q":
            result = [r, col_index]
            break

    if result:
        return result


def move_up_left():
    r, c = king_position()
    result = []
    col_index = c - 1
    for row_index in range(r - 1, -1, -1):
        curr_position = matrix[row_index][col_index]
        if curr_position == ".":
            if col_index > 0:
                col_index -= 1
                continue
            else:
                break
        elif curr_position == "Q":
            result = [row_index, col_index]
            break

    if result:
        return result


def move_up_right():
    r, c = king_position()
    result = []
    col_index = c + 1
    for row_index in range(r - 1, -1, -1):
        curr_position = matrix[row_index][col_index]
        if curr_position == ".":
            if col_index < size - 1:
                col_index += 1
                continue
            else:
                break
        elif curr_position == "Q":
            result = [row_index, col_index]
            break

    if result:
        return result


def move_down_left():
    r, c = king_position()
    result = []
    col_index = c - 1
    for row_index in range(r + 1, size):
        curr_position = matrix[row_index][col_index]
        if curr_position == ".":
            if col_index > 0:
                col_index -= 1
                continue
            else:
                break
        elif curr_position == "Q":
            result = [row_index, col_index]
            break
    if result:
        return result


def move_down_right():
    r, c = king_position()
    result = []
    col_index = c + 1
    for row_index in range(r + 1, size):
        curr_position = matrix[row_index][col_index]
        if curr_position == ".":
            if col_index < size - 1:
                col_index += 1
                continue
            else:
                break
        elif curr_position == "Q":
            result = [row_index, col_index]
            break
    if result:
        return result


matrix = read_matrix()
valid_movements = []

if move_up():
    valid_movements.append(move_up())
if move_down():
    valid_movements.append(move_down())
if move_left():
    valid_movements.append(move_left())
if move_right():
    valid_movements.append(move_right())
if move_up_left():
    valid_movements.append(move_up_left())
if move_up_right():
    valid_movements.append(move_up_right())
if move_down_left():
    valid_movements.append(move_down_left())
if move_down_right():
    valid_movements.append(move_down_right())

if valid_movements:
    for el in valid_movements:
        print(el)
else:
    print("The king is safe!")
