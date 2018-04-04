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

if year%400 == 0 or ( year%4 == 0 and year%100 != 0):
    for i in range(1, month):
        if i == 4 or i == 6 or i == 9 or i == 11:
            n = n + 30
        elif i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10:
            n = n + 31
        elif i == 2:
            n = n + 29
else:
    for i in range(1, month):
        if i == 4 or i == 6 or i == 9 or i == 11:
            n = n + 30
        elif i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10:
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
