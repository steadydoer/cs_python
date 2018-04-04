import time

a = 1
b = 1

n = int(input("Type number : "))

start = time.time()

if n == 1 or n == 2:
    x = 1
else:
    for i in range(n-2):
        x = a + b
        a, b = b, x

print(n, x)
print("Running fibonachi(%d) takes %f" %(n, time.time()-start))

