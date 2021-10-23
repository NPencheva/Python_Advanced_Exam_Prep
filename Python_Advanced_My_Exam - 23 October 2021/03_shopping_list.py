def shopping_list(budget, **kwargs):
    old_dict = kwargs.copy()
    new_list = []
    allowed_amount = 5
    if budget < 100:
        return "You do not have enough budget."
    else:
        for product, value in kwargs.items():
            price, quantity = value
            current_money_spent = price * quantity
            if price * quantity <= budget:
                new_list.append(f"You bought {product} for {current_money_spent:.2f} leva.\n")
                old_dict.pop(product)
                budget -= current_money_spent
            if len(new_list) == allowed_amount or not old_dict:
                break
    result = "".join(el for el in new_list)

    return result


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10),))
print(shopping_list(20, jeans=(19.99, 1), ))
print(shopping_list(104, cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
