import math
print("Type number :", end='')
num = int(input())


for i in range(2, int(math.sqrt(num))):
    if num%i == 0:
        print("%d isn't prime number" %num)
        break
    elif i == num-1:
        print("%d is prime number" %num)
