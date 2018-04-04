import turtle

s = turtle.Screen()
t = turtle.Turtle()
angle = 45



def drawTree(t, lineLength):
    if (lineLength > 0):
        t.forward(lineLength)
        t.left(angle)
        drawTree(t, lineLength-10)
        t.right(angle)
        t.right(angle)
        drawTree(t, lineLength-10)
        t.left(angle)
        t.backward(lineLength)

if __name__ == "__main__":
    lineLength=60
    t.left(90)
    t.pensize(4)
    t.penup()
    t.goto(0, -300)
    t.pendown()
    drawTree(t, lineLength)



 

