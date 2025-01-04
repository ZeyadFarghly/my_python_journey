is_leap_year = True
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_in_month(year, month):
    list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        list[1] = 29
    return list[month-1]

year = int(input("enter the year you want to check: "))
month = int(input("enter the month you want to check of his days: "))
days = days_in_month(year, month)
print(days)
