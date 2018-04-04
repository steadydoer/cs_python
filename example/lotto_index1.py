import random

List = list(range(1, 46))
lot = []

print(List)

a = 44
for i in range(6): #이 부분의 숫자를 바꾸면 뽑는 갯수 달라짐
    b = random.randint(0, a)
    lot.append(List[b])
    del List[b]
    a -= 1

print(lot)

print(sorted(lot))
