def needed_budget(students, flour_price, eggs_price, apron_price):
    from math import ceil

    total_price = 0
    free_flour = students // 5
    total_price += flour_price * (students - free_flour)
    total_price += eggs_price * 10 * students
    total_price += ceil(1.2 * students) * apron_price

    return total_price


budget = float(input())
needed_budget = needed_budget(float(input()), float(input()), float(input()), float(input()))

if budget >= needed_budget:
    print(f"Items purchased for {needed_budget:.2f}$.")
else:
    print(f"{needed_budget - budget:.2f}$ more needed.")
