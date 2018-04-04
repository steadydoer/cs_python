class NumBox:
    def __init__(self, num):
        self.Num = num
    def __add__(self, num):
        #self.Num += num;
        self.Num = self.Num + num.Num
        return self.Num

n = NumBox(1)
m = NumBox(2)
n + m
