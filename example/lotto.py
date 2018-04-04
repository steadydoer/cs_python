import random

lot = []

for i in range(5):
    a = random.randint(1, 45)
    while( a in lot):
        a = random.randint(1, 45)
    lot.append(a)


print(lot)

print(sorted(lot))





#lot_copy = sorted(lot)

#lot_copy.reverse()

#print(lot_copy)

#print(sorted(lot, reverse=True))
