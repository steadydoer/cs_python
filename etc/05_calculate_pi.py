from random import *
from math import sqrt

n = int(input("반복횟수를 입력하시오: "))

in_circular = 0
out_circular = 0
radius = 1
for i in range(n):
    x, y = 2 * random() - 1, 2 * random() - 1  # -1 <= x, y < 1
    if radius >= sqrt(x ** 2 + y ** 2):  # sqrt(x ** 2 + y ** 2)는 원점과 (x, y) 사이의 거리
        in_circular += 1

print("파이 = {}".format(4 * (in_circular / n)))
