import math
print("Type number : ", end='')
n = int(input())

PrimeList = []
for i in range(2, n+1):
    PrimeList.append(i)



for j in range(2, int(math.sqrt(n))+2):
    if j == 2:
        print("%d is prime number" %n)
        for k in range(2, int(n/j)+4):
            if j*k in PrimeList:
                PrimeList.remove(j*k)
    else:
        for i in range(2, int(math.sqrt(n))+2):
            if j%i == 0:
                print("%d isn't prime number" %n)
                break
            elif j == int(math.sqrt(n)+1):
                print("%d is prime number" %n)
                for k in range(2, int(n/j)+4):
                    if j*k in PrimeList:
                        PrimeList.remove(j*k)


print(PrimeList)
