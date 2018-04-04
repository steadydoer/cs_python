print("Enter year :")
year = int(input())

if year%4 == 0 and year%100 !=0:
    print ("%d is leap year"%year)
elif year%400 == 0:
    print ("%d is leap year"%year)
else:
    print("%d is not leap year"%year)
