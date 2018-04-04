#for i in range(10):     #nested for loop
#    for j in range(10):
#        print("*", end="")
#    print()

#print("Type the number of stars.")   #Variable nested loop
#num = int(input())
#for multiplier in range (1, num+1):
#    print('*', end='')

print("Type the number of rows.", end=" ")
r = int(input())
print("Type the number of columns.", end=" ")
c = int(input())

for i in range(1, r+1):
    for j in range(1, c+1):
        print('*', end='')
    print()
