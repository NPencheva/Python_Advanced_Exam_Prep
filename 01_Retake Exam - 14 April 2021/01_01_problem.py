from io import StringIO
import sys
from collections import deque

input1 = """11, 6, 8, 1
3, 1, 9, 10, 5, 9, 1"""
input2 = """10, 9, 8, 7, 5
5, 10, 9, 8, 7"""
input3 = """12, -3, 14, 3, 2, 0
10, 15, 4, 6, 3, 1, 22, 1"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


pizza_orders = deque(int(el) for el in input().split(", "))
employees_capacities = list(map(int, input().split(", ")))
total_pizzas = 0

while pizza_orders:
    if not employees_capacities:
        break
    current_order = pizza_orders.popleft()
    current_capacity = employees_capacities.pop()
    if current_order <= 0 or current_order > 10:
        employees_capacities.append(current_capacity)
        continue
    if current_order <= current_capacity:
        total_pizzas += current_order
    elif current_order > current_capacity:
        new_order = current_order - current_capacity
        pizza_orders.appendleft(new_order)
        total_pizzas += current_capacity

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f'Employees: {", ".join(str(el) for el in employees_capacities)}')
elif not employees_capacities and pizza_orders:
    print("Not all orders are completed.")
    print(f'Orders left: {", ".join(str(el) for el in pizza_orders)}')
