from io import StringIO
import sys
from collections import deque

input1 = """4 5 7 3 6 9 12
12 9 6 1"""
input2 = """3 0 3 6 9 0 12
12 9 6 1 2 3 15 13 4"""
input_test = """4 5 7 3 6 9 12 7 25
12 9 6 1"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input_test)

males = list(map(int, input().split(" ")))
females = deque(int(el) for el in input().split(" "))
successful_matches = 0

while males and females:
    current_male = males.pop()
    current_female = females.popleft()

    if current_male <= 0 or current_female <= 0:
        if current_male <= 0:
            females.appendleft(current_female)
        if current_female <= 0:
            males.append(current_male)
        continue

    if current_male % 25 == 0 or current_female % 25 == 0:
        if current_male % 25 == 0:
            males.pop()
            females.appendleft(current_female)
        if current_female % 25 == 0:
            females.popleft()
            males.append(current_male)
        continue

    if current_male == current_female:
        successful_matches += 1
    else:
        males.append(current_male - 2)

print(f"Matches: {successful_matches}")

if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(str(el) for el in reversed(males))}")

if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(str(el) for el in females)}")
