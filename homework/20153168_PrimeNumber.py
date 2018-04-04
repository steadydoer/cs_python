import math

print("Type number : ", end='')
n = int(input())

if n == 1:
    print("%d isn't prime number" %n)
else:
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            print("%d isn't prime number" %n)
            break
    else :
        print("%d is prime number" %n)
