print("Type Number.", end=' ')
n = int(input())


for i in range(1, n+1):
    for j in range(i):
        print(i + (n-1+n-j)*j//2, end = "  ")
    print()

