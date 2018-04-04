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
def HanoiTower(ap, bp, cp):
    if len(ap) == 1 and len(cp) == 0:
        cp.append(ap.pop())
        d[0] = d[0] + 1
        if len(bp) == 1:
            HanoiTower(b, a, c)
        elif len(bp) > 1:
            HanoiTower(b, c, a)
        print("Count number = ", d)
    else :
        if len(ap)%2 == 0 and len(ap) != 0:
            bp.append(ap.pop())
            d[0] = d[0] + 1
            HanoiTower(a, b, c)
        elif len(ap)%2 == 1 and len(ap) != 0:
            if len(ap) == 1:
                bp.append(cp.pop())
                d[0] = d[0] + 1
                HanoiTower(a, b, c)
            else:
                cp.append(ap.pop())
                d[0] = d[0] + 1
                HanoiTower(a, b, c)


    """elif len(b) == 1 and len(c) ==0:
        c.append(b.pop())
    elif len(a)%2 == 0 and len(a) != 0:
        b.append(a.pop())
        c.append(a.pop())
        HanoiTower(a, b, c)"""




#Main program

HanoiTower(a, b, c)
print(a)
print(b)
print(c)

