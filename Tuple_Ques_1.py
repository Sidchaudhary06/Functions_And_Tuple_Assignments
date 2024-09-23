
def get_season(month):
    seasons = ("Winter", "Spring", "Summer", "Autumn")


    if month in (12, 1, 2):  # December, January, February -> Winter
        return seasons[0]
    elif month in (3, 4, 5):  # March, April, May -> Spring
        return seasons[1]
    elif month in (6, 7, 8):  # June, July, August -> Summer
        return seasons[2]
    elif month in (9, 10, 11):  # September, October, November -> Autumn
        return seasons[3]
    else:
        return "Invalid month number."



def Ques_1():

    month = int(input("Enter the number of the month (1-12): "))


    season = get_season(month)


    print(f"The corresponding season is: {season}")

Ques_1()
