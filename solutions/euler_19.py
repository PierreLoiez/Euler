
def Euler19():
    sundays = 0
    year = 1900
    month = 1
    day = 1
    dayOfTheWeek = 0
    months30days = [9, 4, 6, 11]
    while year < 2000 or day<31 or month<12:
        if month in months30days and day == 30:
            day = 1
            month += 1
        elif (
            month == 2
            and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
            and day == 29
        ):
            day = 1
            month += +1
        elif month == 2 and day == 28:
            day = 1
            month += 1
        elif day==31:
            day=1
            month = month%12+1
            if month == 1:
                year += 1
        else:
            day += 1
        dayOfTheWeek = (dayOfTheWeek+1)%7
        if day==1 and dayOfTheWeek==6 and year>1900:
            sundays+=1
    return sundays

print(Euler19())
