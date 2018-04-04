"""
HanoiTower(1, a, b, c)
# n = 1, g1 = a, g2 = b, g3 = c
g3.append(g1.pop()) # c.append(a.pop())
#end of function // v[1] == a, v[2] == b, v[3] == c
 

HanoiTower(2, a, b, c) # HT(1, a, c, b) -> c.append(a.pop()) -> HT(1, b, a, c)
# n = 2, g1 = a, g2 = b, g3 = c
v[1] = g1
v[2] = g3
v[3] = g2 # v[1] == a, v[2] == c, v[3] == b
HanoiTower(n-1, v[1], v[2], v[3]) # HT(1, a, c, b)
g3.append(g1.pop()) # c.append(a.pop())
HanoiTower(n-1, v[3], v[1], v[2]) # HT(1, b, a, c)
#end of function // v[1] == a, v[2] == c, v[3] == b
#( a -> a, b -> c, c -> b)


HanoiTower(3, a, b, c) # HT(2, a, c, b) -> c.append(a.pop()) -> HT(2, b, a, c)
# n = 3, g1 = a, g2 = b, g3 = c
v[1] = g1
v[2] = g3
v[3] = g2 # v[1] == a, v[2] == c, v[3] == b
HanoiTower(n-1, v[1], v[2], v[3]) # HT(2, a, c, b)
g3.append(g1.pop()) # c.append(a.pop()) // v[1] == a, v[2] == b, v[3] == c
HanoiTower(n-1, v[2], v[1], v[3]) # HT(2, b, a, c)
#end of function // v[1] == b, v[2] == c, v[3] == a
# ( a -> b, b -> c, c -> a)


HanoiTower(4, a, b, c) # HT(3, a, c, b) -> c.append(a.pop()) -> HT(3, b, a, c)
# n = 4, g1 = a, g2 = b, g3 = c
v[1] = g1
v[2] = g3
v[3] = g2 # v[1] == a, v[2] == c, v[3] == b
HanoiTower(n-1, v[1], v[2], v[3]) # HT(3, a, c, b)
g3.append(g1.pop()) # c.append(a.pop()) // v[1] == c, v[2] == b, v[3] == a
HanoiTower(n-1, v[2], v[3], v[1]) # HT(3, b, a, c)
#end of function // v[1] == a, v[2] == c, v[3] == b
#( a -> a, b -> c, c -> b)


HanoiTower(5, a, b, c) # HT(4, a, c, b) -> c.append(a.pop()) -> HT(4, b, a, c)
# n = 5, g1 = a, g2 = b, g3 = c
v[1] = g1
v[2] = g3
v[3] = g2 # v[1] == a, v[2] == c, v[3] == b
HanoiTower(n-1, v[1], v[2], v[3]) # HT(4, a, c, b)
g3.append(g1.pop()) # c.append(a.pop()) // v[1] == a, v[2] == b, v[3] == c
HanoiTower(n-1, v[2], v[1], v[3]) # HT(4, b, a, c)
#end of function // v[1] == b, v[2] == c, v[3] == a
#( a -> b, b -> c, c -> a)


HanoiTower(6, a, b, c) # HT(5, a, c, b) -> c.append(a.pop()) -> HT(5, b, a, c)
# n = 5, g1 = a, g2 = b, g3 = c
v[1] = g1
v[2] = g3
v[3] = g2 # v[1] == a, v[2] == c, v[3] == b
HanoiTower(n-1, v[1], v[2], v[3]) # HT(5, a, c, b)
g3.append(g1.pop()) # c.append(a.pop()) // v[1] == c, v[2] == b, v[3] == a
HanoiTower(n-1, v[2], v[3], v[1]) # HT(5, b, a, c)
#end of function // v[1] == a, v[2] == c, v[3] == b
#( a -> a, b -> c, c -> b)

"""

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
def HanoiTower(n, g1, g2, g3):    
    if n == 1:
        g3.append(g1.pop())
        print("a, b, c =",a, b, c)
        print("v[1], v[2], v[3] =", v[1], v[2], v[3])
        m[0] += 1
        print("Number of moves : ", m[0])
    else:
        if n%2 == 0:
            v[1] = g1
            v[2] = g3
            v[3] = g2
            HanoiTower(n-1, v[1], v[2], v[3])
            g3.append(g1.pop())
            print("a, b, c =",a, b, c)
            print("v[1], v[2], v[3] =", v[1], v[2], v[3])
            m[0] += 1
            print("Number of moves : ", m[0])            
            if n != 2:
                HanoiTower(n-1, v[2], v[3], v[1])
            else:
                HanoiTower(n-1, v[3], v[1], v[2])
        elif n%2 == 1:
            v[1] = g1
            v[2] = g3
            v[3] = g2
            HanoiTower(n-1, v[1], v[2], v[3])
            g3.append(g1.pop())
            print("a, b, c =",a, b, c)
            print("v[1], v[2], v[3] =", v[1], v[2], v[3])
            m[0] += 1
            print("Number of moves : ", m[0])
            HanoiTower(n-1, v[2], v[1], v[3])
            

        
#Main program
HanoiTower(rings, a, b, c)
print("a = ",a)
print("b = ",b)
print("c = ",c)
