def best_list_pureness(my_list, k):
    best_pureness = 0
    current_pureness = 0
    best_rotation_count = 0

    for rotation in range(k):
        for index, value in enumerate(my_list):
            current_pureness += (index * value)

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation_count = rotation
        current_pureness = 0
        my_list.insert(0, my_list.pop())

    return f"Best pureness {best_pureness} after {best_rotation_count} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

test = ([0, 0, 0, 0], 3)
result = best_list_pureness(*test)
print(result)