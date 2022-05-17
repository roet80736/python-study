import turtle
turtle.pencolor("red")
turtle.pensize(6)
for i in range (0,24):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.seth(0)
    turtle.seth(15 * i)
    turtle.pendown()
    turtle.circle(-100, -90)
turtle.mainloop()