n = 0
print ("Type year : ", end='')
year = int(input())
while(year < 1):
    print ("Check the year that you type.")
    print ("Type year : ", end='')
    year = int(input())
    
print ("Type month : ", end='')
month = int(input())
while(month < 1 or month > 12):
    print ("Check the month that you type.")
    print ("Type month : ", end='')
    month = int(input())


# 30 : 4, 6, 9, 11 // 31: 1, 3, 5, 7, 8, 10, 12 // 28: 2 // 29: 2

print ("Type day : ", end='')
day = int(input())
if year%400 == 0 or ( year%4 == 0 and year%100 != 0):
    if month == (4 or 6 or 9 or 11):
        while (day < 1 or day > 30):
            print("Check the day that you type.")
            print("Type day : ", end='')
            day = int(input())
    elif month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        while (day < 1 or day > 31):
            print("Check the day that you type.")
            print("Type day : ", end='')
            day = int(input())
    elif month == 2:
        while (day < 1 or day > 29):
            print("Check the day that you type.")
            print("Type day : ", end='')
            day = int(input())
else:
    if month == (4 or 6 or 9 or 11):
        while (day < 1 or day > 30):
            print("Check the day that you type.")
            print("Type day : ", end='')
            day = int(input())
    elif month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        while (day < 1 or day > 31):
            print("Check the day that you type.")
            print("Type day : ", end='')
            day = int(input())
    elif month == 2:
        while (day < 1 or day > 28):
            print("Check the day that you type.")
            print("Type day : ", end='')
            day = int(input())


for i in range(1, year):
    if i%400 == 0 or ( i%4 == 0 and i%100 != 0):
        n = n + 366
    else:
        n = n + 365
   

if year%400 == 0 or ( year%4 == 0 and year%100 != 0):
    for i in range(1, month):
        if i == (4 or 6 or 9 or 11):
            n = n + 30
        elif i == (1 or 3 or 5 or 7 or 8 or 10):
            n = n + 31
        elif i == 2:
            n = n + 29
else:
    for i in range(1, month):
        if i == (4 or 6 or 9 or 11):
            n = n + 30
        elif i == (1 or 3 or 5 or 7 or 8 or 10):
            n = n + 31
        elif i == 2:
            n = n + 28


n = n + day


if ( n%7 ) == 0:
    print("%d.%d.%d is Sunday."%(year, month, day))
elif ( n%7 ) == 1:
    print("%d.%d.%d is Monday."%(year, month, day))
elif ( n%7 ) == 2:
    print("%d.%d.%d is Tuesday."%(year, month, day))
elif ( n%7 ) == 3:
    print("%d.%d.%d is Wednessday."%(year, month, day))
elif ( n%7 ) == 4:
    print("%d.%d.%d is Thursday."%(year, month, day))
elif ( n%7 ) == 5:
    print("%d.%d.%d is Friday."%(year, month, day))
elif ( n%7 ) == 6:
    print("%d.%d.%d is Saturday."%(year, month, day))
