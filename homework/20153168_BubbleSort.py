import time
import random


print("Type length of list : ", end='')
n = int(input())
List = []


for i in range(n):
    List.append(random.randint(0, n*10))

List_bubble = List[:]

start = time.time()
List.sort()
end = time.time()
print("Running sort(%d) takes is %s" %(n, end-start))


start = time.time()
for i in range( len(List_bubble)-1 ):
    for j in range( len(List_bubble)-1 - i):
        if (List_bubble[j] > List_bubble[j+1]):
            t = List_bubble[j]
            List_bubble[j] = List_bubble[j+1]
            List_bubble[j+1] = t
end = time.time()

print("Running Bubble sort(%d) takes is %s" %(n, end-start))
