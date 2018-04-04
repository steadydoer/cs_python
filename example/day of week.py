n = 0
print ("Type year : ", end='')
year = int(input())
print ("Type month : ", end='')
month = int(input())
print ("Type day : ", end='')
day = int(input())

for i in range(1, year+1):
    if i == year:
        break
    elif i%400 == 0 or ( i%4 == 0 and i%100 != 0):
        n = n + 366
    else:
        n = n + 365

#print("Year plus is %d" %n)

if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    if month == 1:
        n = n
    elif month == 2:
        n = n + 31
    elif month == 3:
        n = n + 60
    elif month == 4:
        n = n + 91
    elif month == 5:
        n = n + 121
    elif month == 6:
        n = n + 152
    elif month == 7:
        n = n + 182
    elif month == 8:
        n = n + 213
    elif month == 9:
        n = n + 244
    elif month == 10:
        n = n + 274
    elif month == 11:
        n = n + 305
    elif month == 12:
        n = n + 335
    else:
        n = n
else:
    if month == 1:
        n = n
    elif month == 2:
        n = n + 31
    elif month == 3:
        n = n + 59
    elif month == 4:
        n = n + 90
    elif month == 5:
        n = n + 120
    elif month == 6:
        n = n + 151
    elif month == 7:
        n = n + 181
    elif month == 8:
        n = n + 212
    elif month == 9:
        n = n + 243
    elif month == 10:
        n = n + 273
    elif month == 11:
        n = n + 304
    elif month == 12:
        n = n + 334
    else:
        n = n


#print ("N is %d" %n)

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
