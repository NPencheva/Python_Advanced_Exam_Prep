def stock_availability(inv_list, action, *args):
    arguments = [el for el in args]
    if len(arguments) == 0:
        inv_list.pop(0)
    for item in arguments:
        if action == "delivery":
            inv_list.append(item)
        if action == "sell":
            try:
                for box in range(item):
                    inv_list.pop(0)
            except TypeError:
                if item in inv_list:
                    inv_list = [el for el in inv_list if el != item]

    return inv_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
