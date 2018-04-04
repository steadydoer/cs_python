import random

def bubblesort(List_bubble):
    for i in range( len(List_bubble)-1 ):
        for j in range( len(List_bubble)-1 - i):
            if (List_bubble[j] > List_bubble[j+1]):
                t = List_bubble[j]
                List_bubble[j] = List_bubble[j+1]
                List_bubble[j+1] = t

List = []
lot = []
for i in range(1, 46):
    List.append(i)

print(List)
for i in range(5):
    a = 44
    b = random.randint(0, a)
    lot.append(List[b])
    del List[b]
    a -= 1
    
print(lot)
               
bubblesort(lot)

print(lot)




#print(lot)

#lot_copy = sorted(lot)

#print(sorted(lot))

#lot_copy.reverse()

#print(lot_copy)

#print(sorted(lot, reverse=True))
