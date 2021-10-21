def get_magic_triangle(n):
    magic_triangle = [[1], [1, 1]]
    for row_index in range(2, n):
        magic_triangle.append([])
        magic_triangle[-1].append(1)
        for col_index in range(1, row_index):
            left = magic_triangle[row_index - 1][col_index - 1]
            right = magic_triangle[row_index - 1][col_index]
            magic_triangle[-1].append(left + right)
        magic_triangle[-1].append(1)

    return magic_triangle


print(get_magic_triangle(5))
