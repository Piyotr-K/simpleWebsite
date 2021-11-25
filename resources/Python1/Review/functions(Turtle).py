import turtle

def polygon(sides, color = "black", size = 100):
    t1.color(color)
    for x in range(sides):
        t1.forward(size)
        t1.right(360 / sides)

t1 = turtle.Turtle()
t1.speed(0)

# When using functions/method, type the name and followed by brackets
# Actual Parameters have to match the order of the Formal Parameters
polygon(8, "red")

turtle.mainloop()