#Created by YongHua
import calendar
import time

while True:
    print("This is Python calendar.")

    while True:
        try:
            year = int(input("Please enter a year. >> "))
            if 1900 <= year <= 2999:
                break
            else:
                print("Please enter a year between 1900 and 2999.")

        except:
            print("This is not a valid number.")


    while True:
        try:
            month = int(input("Please enter a month. >> "))
            if 1 <= month <= 12:
                break
            else:
                print("Please enter a month between 1 and 12.")

        except:
            print("This is not a valid number.")


    print(calendar.month(year, month))

    print("Type '0' to exit.")
    try:
        x = int(input("Please enter a code. >> "))
        if x == 0:
            break
        else:
             pass

    except:
        pass
