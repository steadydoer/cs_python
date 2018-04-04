import math
print("Input n:", end=' ')
n=int(input())
PrimeNumberList=[]



for i in range(2 ,n+1):
    for j in range(2, int(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        PrimeNumberList.append(i)


#for i in range(1,n+1):
#    for j in range(2, int(math.sqrt(i))+1):
#        if n%j==0:
#            print()
#        else:
#            PrimeNumberList.append(j)


print(PrimeNumberList)
