# Declare variables
a = []
b = []
c = []
d = [0]

#input number of rings
print("Type number of rings.", end=' ')
n = int(input())
while( n <= 0):
    print("Type number of rings.", end=' ')
    n = int(input())

#Make list
for i in range(n):
    a.append(n-i)

#Define function
def HanoiTower(np, a, b, c):
    ap = a[:]
    bp = b[:]
    cp = c[:]
    if np == 1:
        cp.append(ap.pop())
        d[0] += 1
        if len(ap) == 0 and len(bp) == 1:
            cp.append(bp.pop())
            d[0] += 1
            print("Count number = ", d)
        elif len(ap) == 1 and len(bp) == 0:
            cp.append(ap.pop())
            d[0] += 1
            print("Count number = ", d)
        else:
            print("Count number = ", d)
    else :
        if np%2 == 0:
            bp.append(ap.pop())
            d[0] += 1
            np -= 1
            HanoiTower(np, a, b, c)
        elif np%2 == 1:
            HanoiTower(np-1, a, c, b)
            cp.append(ap.pop())
            HanoiTower(np-1, b, a, c)
            
            
            


    """elif len(b) == 1 and len(c) ==0:
        c.append(b.pop())
    elif len(a)%2 == 0 and len(a) != 0:
        b.append(a.pop())
        c.append(a.pop())
        HanoiTower(a, b, c)"""




#Main program

HanoiTower(n, a, c, b)
print(a)
print(b)
print(c)

