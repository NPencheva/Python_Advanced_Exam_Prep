from io import StringIO
import sys

input1 = """10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)"""
input2 = """B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)"""
input_test = """B 30 14 23 20 24
B 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input_test)


def read_matrix():
    this_matrix = []

    for _ in range(size):
        row = [x for x in input().split(" ")]
        this_matrix.append(row)

    return this_matrix


def check_is_in_board():
    if coord_row < 0 or coord_col < 0 or coord_row >= size or coord_col >= size:
        return False
    else:
        return True


size = 6
matrix = read_matrix()
times_thrown = 0
points_scored = 0
coord_history = []
is_winner = False
prize = ""

while times_thrown < 3:
    coord_row, coord_col = [int(el) for el in input().strip("()").split(", ")]
    times_thrown += 1
    coord_hit = (coord_row, coord_col)
    if check_is_in_board():
        point_hit = matrix[coord_row][coord_col]
        if point_hit != "B":
            continue
        if coord_hit in coord_history:
            continue
        else:
            for row_index in range(size):
                col_index = coord_col
                current_point = matrix[row_index][col_index]
                if current_point != "B":
                    points_scored += int(current_point)
            matrix[coord_row][coord_col] = "0"


if points_scored >= 100:
    is_winner = True
    if 100 <= points_scored <= 199:
        prize = "Football"
    elif 200 <= points_scored <= 299:
        prize = "Teddy Bear"
    elif points_scored >= 300:
        prize = "Lego Construction Set"

if is_winner:
    print(f"Good job! You scored {points_scored} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - points_scored} points more to win a prize.")


