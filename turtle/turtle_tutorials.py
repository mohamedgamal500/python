import turtle
arrow = turtle.Turtle()
arrow.color("red", "yellow")
arrow.speed(10)

arrow.begin_fill()
for i in range(100):
    arrow.forward(100)
    arrow.left(170)
    arrow.forward(100)
arrow.end_fill()


turtle.done()
