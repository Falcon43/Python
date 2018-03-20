#turtle standard graphics library for python
import turtle

window = turtle.Screen()
window.title("Equilateral triangle")

print(turtle.position())
turtle.penup()
turtle.setx(-150)
turtle.sety(+150)
turtle.pendown()
print(turtle.position())
turtle.forward(300)
turtle.right(120)
turtle.forward(300)
turtle.right(120)
turtle.forward(300)

turtle.done()

