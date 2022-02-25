
month = int(input("month?"))
year = int(input("year?"))


def leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False



def month_days(month,year):
    month_30 = [4,6,9,11]
    days = 31
    if month == 2:
        if leap(year):
            days=29
        else:
            days = 28
    elif month in month_30:
        days =30
    return days
        

def cul(month,year):
    zenjitu=0
    for i in range(1900,year):
        if leap(i):
            zenjitu=zenjitu+366
        else:
            zenjitu = zenjitu + 365
    for j in range(1,month):
        zenjitu= zenjitu+ month_days(j,year)
    return zenjitu







print("msun\tmon\ttue\twed\tthr\tfry\tsat")
zenjitu=cul(month,year)%7+1
for i in range(zenjitu%7):
    print("\t",end="")
for j in range(1,month_days(month,year)+1):
    print(j,"\t",end="")
    zenjitu = zenjitu +1
    if zenjitu%7==0:
        print("")




























