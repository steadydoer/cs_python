print("Type n :", end='')
n = int(input())
for i in range(1, n+1): # i == 1, 2, 3, ..., n
    for j in range(1, i+1): # j == 1, 2, ..., i
        print('*', end='')
    print()

print()

"""for i in range(n): # i == 0, 1, 2, ..., n-1
    for j in range(i+1): # j == 0, 1, ..., i
        print('*', end='')
    print()

print()

for i in range(1, n+1):
    j = i*'*'
    print('%s' %j)
print()"""
    

