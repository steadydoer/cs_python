print("Type small number first, then big number.")
print("a=", end=" ")
a=int(input())
print("b=", end=" ")
b=int(input())
#for u in range(a, b+1):
#    for multiplier in range (1, 10):
#        print (u, "x", multiplier, "=", u * multiplier, end="   ")
#    print()

while(a != b+1):
    x = 1
    while(x != 10):
        print(a, "x", x, "=", a * x)
        x = x+1
    a = a+1
