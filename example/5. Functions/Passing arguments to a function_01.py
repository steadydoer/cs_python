# Define a function
def printPerson(name, num):
    name = "S Lee"
    num = 618
    pName = 112
    pNum = 113
    print("In the fucn.:", name, num)
    print("In the fucn.:", pName, pNum)

def mutableArgument(names):
    names.append("Bob")
    names.sort()
    print("In the func.:", names)

# main program
pName = "M yoon"
pNum = 616
print("Before the func.:", pName, pNum)
printPerson(pName, pNum)
print("Afrter the func.:", pName, pNum)

pNames = ["Dave", "Alice"]
print("Before the func.:", pNames)
mutableArgument(pNames)
print("After the func.:", pNames)
