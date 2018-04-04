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
def HanoiTower(np, resource, via, target):
    if np == 1:
        if len(resource) != 0:
            target.append(resource.pop())
            d[0] += 1
            print("Count number = ", d)
            print(a)
            print(b)
            print(c)
        else:
            print("Count number = ", d)
    else :
        if np in range(2, n+1):
            np -= 1
            HanoiTower(np, resource, target, via)
            c.append(a.pop())
            d[0] += 1
            print("Count number = ", d)
            print(a)
            print(b)
            print(c)
            HanoiTower(np, via, resource, target)
        #print("Count number = ", d)
        
            
            
            


    """elif len(b) == 1 and len(c) ==0:
        c.append(b.pop())
    elif len(a)%2 == 0 and len(a) != 0:
        b.append(a.pop())
        c.append(a.pop())
        HanoiTower(a, b, c)"""




#Main program

HanoiTower(n, a, b, c)
#print(a)
#print(b)
#print(c)

