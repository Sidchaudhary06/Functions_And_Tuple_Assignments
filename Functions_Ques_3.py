def gallons_to_liters(gallons):
    liters = gallons * 3.78541  # 1 gallon is approximately 3.78541 liters
    return liters


def Ques_2():
    while True:
        gallons = float(input("Enter the volume in gallons (or a negative number to quit): "))

        if gallons < 0:
            print("Exiting the program.")
            break

        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is equal to {liters:.2f} liters.")



Ques_2()
