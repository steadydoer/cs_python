import math
print("Type number : ", end='')
n = int(input())

PrimeList = []

for i in range (2, n+1):
    if i == 2:
        PrimeList.append(i)
    for k in range(2, int(math.sqrt(i)+2)):
        if i%k == 0:
            break
    else :
        PrimeList.append(i)


print(PrimeList)
