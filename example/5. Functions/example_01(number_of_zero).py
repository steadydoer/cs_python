print("Type Number.", end=' ')
n = int(input())

x = 0


#while( n >= 10):
if n == 0:
    x =+ 1
else:
    while n%10 == 0 :
        r = n%10
        if r == 0:
            x += 1
        n = int(n/10)
    

print("Number of zero is %d" %x)
