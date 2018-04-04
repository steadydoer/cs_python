import sys

sys.path.append("/home/user/example")


import my_vector

# my_vector 모듈의 vec2 클래스 활용
a = my_vector.vec2(9,0) 
b = my_vector.vec2(-1, -2) 
c = a + b 

print(c)
