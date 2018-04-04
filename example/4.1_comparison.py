a = [13, 4, 7, 5, 9, 3]
small = a[0]
print(len(a))
for i in range(1, len(a)):
    if small >= a[i]:
        small = a[i]

print(small)
