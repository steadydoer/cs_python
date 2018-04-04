class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

myBall = Ball("red", "small", "down")#클래스 이름만 입력하면 생성자 메서드를 찾아 실행함
print(myBall)
