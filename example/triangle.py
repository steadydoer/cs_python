print("Enter x, y, z(x <= y <= z)")
print("Enter x : ")
x = int(input())
print("Enter y : ")
y = int(input())
print("Enter z : ")
z = int(input())


if x + y <= z:
    print("3")
elif x**2 + y**2 > z**2:
    print("0")
elif x**2 + y**2 == z**2:
    print("1")
else:
    print("2")
