import math


def pizza_unit_price(diameter_cm, price_euros):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = math.pi * radius_m ** 2
    unit_price = price_euros / area_m2
    return unit_price


def Ques_6():

    diameter1 = float(input("Enter the diameter of the first pizza in cm: "))
    price1 = float(input("Enter the price of the first pizza in euros: "))


    diameter2 = float(input("Enter the diameter of the second pizza in cm: "))
    price2 = float(input("Enter the price of the second pizza in euros: "))


    unit_price1 = pizza_unit_price(diameter1, price1)
    unit_price2 = pizza_unit_price(diameter2, price2)

    print(f"\nThe unit price of the first pizza is: {unit_price1:.2f} euros per square meter.")
    print(f"The unit price of the second pizza is: {unit_price2:.2f} euros per square meter.")


    if unit_price1 < unit_price2:
        print("\nThe first pizza provides better value for money.")
    elif unit_price1 > unit_price2:
        print("\nThe second pizza provides better value for money.")
    else:
        print("\nBoth pizzas offer the same value for money.")

Ques_6()
