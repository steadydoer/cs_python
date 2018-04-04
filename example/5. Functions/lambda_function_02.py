"""
a = "Kookmin Univ. is leading the computer science".split()

print(a)
a.sort()
print(a)
a.sort(key=str.upper)
print(a)
a.sort(key=str.upper, reverse=True)
print(a)
"""
"""
b = ["34", "123", "7"]
b.sort()
print(b)
b.sort(key=int)
print(b)
"""
a = [("Yoon", 2010), ("Lee", 2006), ("Lim", 2004)]
a.sort(key = lambda x : x[1])
print(a)
