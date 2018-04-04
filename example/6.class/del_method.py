class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def __del__(self):
        print("Class is deleted!")

myBall = Ball("red", "small", "down")#클래스 이름만 입력하면 생성자 메서드를 찾아 실행함
