
def leapyear(year):
    """Check Wheather Year is Leap Or Not"""
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def dayinmonth(year,month):
    if leapyear(year):
        monthdays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return monthdays[month - 1]
    else:
        monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return monthdays[month - 1]


year=int(input("Enter a Year :"))
month=int(input("Enter a month :"))
days=dayinmonth(year,month)
print(days)