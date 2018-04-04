# Define a function

def f1():
    print ("f1 starts")
    f2()
    print ("f1 ends")

def f2():
    print ("f2 starts")
    f3()
    print ("f2 ends")

def f3():
    print ("f3 starts")
    print ("f3 ends")

#main program

print("program starts")
f1()
print("program ends")
