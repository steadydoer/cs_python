#Declare variables
a = []
b = []
c = []
m = [0] # Number of moves
v = [0, a, b, c] # Mutable variable in function


#Input number of rings
print("Type number of rings.", end=' ')
rings = int(input())


#Make List
for i in range(rings):
    a.append(rings-i)


#Define function
#n is number of rings, g1 is a point of departure
#g2 is using point and g3 is destination
def HanoiTower(n, g1, g2, g3):
    if n == 1:
        g3.append(g1.pop())
        print(a)
        print(b)
        print(c)
        m[0] += 1
    else:
        v[1] = g1
        v[2] = g3
        v[3] = g2
        if n%2 == 0:
            HanoiTower(n-1, v[1], v[2], v[3])
            g3.append(g1.pop())
            print(a)
            print(b)
            print(c)
            m[0] += 1
            if n == 2:
                HanoiTower(n-1, v[3], v[1], v[2])
            else:
                HanoiTower(n-1, v[2], v[3], v[1])
        else:
            HanoiTower(n-1, v[1], v[2], v[3])
            g3.append(g1.pop())
            print(a)
            print(b)
            print(c)
            m[0] += 1
            HanoiTower(n-1, v[2], v[1], v[3])
            

        
#Main program
HanoiTower(rings, a, b, c)
print("a = ",a)
print("b = ",b)
print("c = ",c)
print("Number of moves : ", m[0])
