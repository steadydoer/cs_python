family = ['엄마', '아빠', '형', '동생']
print (family)

family.append('baby')
print (family[0])
print (family[1])
print (family[2])
print (family[3])

print (family[4])
print (family[-1])

print (family[0:3])
print (family[3:6])
print (family[:3])
print (family[3:])


print(type(family[1]))
print(type(family[1:4]))

family.append("uncle")
family.insert(0, "grand master")
family.extend([1 , 2, 3])

print(family)

family.remove('baby')
family.remove(1)
family.remove(2)
del family[0]
x = family.pop()
print(family)
print(x)

print('uncle' in family)
if 1 in family:
    print("There is '1'")
else:
    print("There isn't '1'")

family_copy = family[:]
family_copy.sort()
print(family)
print(family_copy)
