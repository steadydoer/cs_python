import math

print("Type number : ", end='')
n = int(input())

if n == 1:
    print("%d isn't prime number" %n)
elif n == 2:
    print("%d is prime number" %n)
else:
    for i in range(2, int(math.sqrt(n))+2):
        if n%i == 0:
            print("%d isn't prime number" %n)
            break
        elif i == int(math.sqrt(n)+1):
            print("%d is prime number" %n)
