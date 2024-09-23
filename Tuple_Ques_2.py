
def Ques_2():

    names_set = set()

    while True:

        name = input("Enter a name (or press Enter to stop): ")


        if name == "":
            break


        if name in names_set:
            print("Existing name")
        else:
            print("New name")
            names_set.add(name)


    print("\nThe entered names are:")
    for name in names_set:
        print(name)



Ques_2()
