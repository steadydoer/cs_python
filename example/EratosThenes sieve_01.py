print("Type number : ", end='')
n = int(input())

PrimeList = []
for i in range(2, n+1):
    PrimeList.append(i)



for j in PrimeList:
    k = 2
    while( j*k <=n ):
        if j*k in PrimeList:
            PrimeList.remove(j*k)
        k += 1
    #print(j)
    #print(PrimeList)


print(PrimeList)
