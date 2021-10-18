from io import StringIO
import sys
from collections import deque

input1 = """5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22"""
input2 = """-15, -8, 0, -16, 0, -22
10, 5"""
input3 = """1, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 1"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


firework_effects = deque(int(el) for el in input().split(", "))
explosive_power = list(map(int, input().split(", ")))
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
show_target = 3
is_perfect_show = False

while firework_effects and explosive_power:
    current_firework = firework_effects.popleft()
    current_explosive_power = explosive_power.pop()

    if current_firework <= 0 or current_explosive_power <= 0:
        if current_firework <= 0:
            explosive_power.append(current_explosive_power)
        if current_explosive_power <= 0:
            firework_effects.appendleft(current_firework)
        continue

    if (current_firework + current_explosive_power) % 3 == 0 and (current_firework + current_explosive_power) % 5 != 0:
        palm_fireworks += 1
    elif (current_firework + current_explosive_power) % 3 != 0 and (current_firework + current_explosive_power) % 5 \
            == 0:
        willow_fireworks += 1
    elif (current_firework + current_explosive_power) % 3 == 0 and (current_firework + current_explosive_power) % 5 \
            == 0:
        crossette_fireworks += 1
    else:
        current_firework -= 1
        firework_effects.append(current_firework)
        explosive_power.append(current_explosive_power)

    if palm_fireworks >= show_target and willow_fireworks >= show_target and crossette_fireworks >= show_target:
        is_perfect_show = True
        break

if is_perfect_show:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(el) for el in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(el) for el in explosive_power)}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
