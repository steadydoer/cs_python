import time
def fibonachi(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)


n = int(input("Type number :"))

start = time.time()
print(n, fibonachi(n))
print("Running fibonachi(%d) takes %f" %(n, time.time()-start))
