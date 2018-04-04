from math import sin
from math import pi

# math 모듈의 함수 sin()와 상수 pi를 현재 네임스페이스로 활용
print("PI = {0}".format(pi)) 

# math 모듈의 함수를 현재 네임스페이스로 활용
val = sin(pi / 2) 
print("sin(PI/2) = {0}".format(val)) 
#val = math.cos(pi / 2) 
#print("cos(PI/2) = {0}".format(val))
