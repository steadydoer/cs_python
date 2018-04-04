def sigma(n):
    if n == 1:
        return n
    else:
        return n + sigma(n-1)

n = int(input("Type number :"))

print(n, sigma(n))
