from io import StringIO
import sys
from collections import deque

input1 = """105 20 30 25
120 60 11 400 10 1"""
input2 = """30 5 21 6 0 91
15 9 5 15 8"""
input3 = """200
5 15 32 20 10 5"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)


def calculate_present():
    is_it_crafted = True
    if 100 <= current_value <= 199:
        crafted_presents_dict["Gemstone"] += 1
    elif 200 <= current_value <= 299:
        crafted_presents_dict["Porcelain Sculpture"] += 1
    elif 300 <= current_value <= 399:
        crafted_presents_dict["Gold"] += 1
    elif 400 <= current_value <= 499:
        crafted_presents_dict["Diamond Jewellery"] += 1
    else:
        is_it_crafted = False
    return is_it_crafted


materials = [int(el) for el in input().split(" ")]
magic_level = deque(int(el) for el in input().split(" "))
is_crafted = False

crafted_presents_dict = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    current_value = current_material + current_magic

    if calculate_present():
        continue
    else:
        if current_value < 100:
            if current_value % 2 == 0:
                current_material *= 2
                current_magic *= 3
                current_value = current_material + current_magic
                if calculate_present():
                    continue
            elif current_value % 2 != 0:
                current_value *= 2
                if calculate_present():
                    continue
        elif current_value > 499:
            current_value /= 2
            if calculate_present():
                continue
        else:
            is_crafted = False
            continue


if (crafted_presents_dict["Gemstone"] > 0 and crafted_presents_dict["Porcelain Sculpture"] > 0) or (
        crafted_presents_dict["Gold"] > 0 and crafted_presents_dict["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(el) for el in materials])}")
if magic_level:
    print(f"Magic left: {', '.join([str(el) for el in magic_level])}")

for key, value in sorted(crafted_presents_dict.items()):
    if value > 0:
        print(f"{key}: {value}")
