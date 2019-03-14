import turtle

def print_digits(number,length):
    if number == 0:
        turtle.forward(length*2)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length*2)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length*2)
    if number == 1:
        turtle.forward(length*2)
    if number == 2:
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.backward(length/2)
        turtle.right(90)
    if number == 3:
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.backward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)
    if number == 4:
        turtle.right(45)
        turtle.forward(length*1.5)
        turtle.left(135)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length/2)
        turtle.backward(length/2)
        turtle.left(180)
        turtle.forward(length)
    if number == 5:
        turtle.left(90)
        turtle.backward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)
    if number == 6:
        turtle.left(90)
        turtle.backward(length)
        turtle.right(90)
        turtle.forward(length*2)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.penup()
        turtle.left(90)
        turtle.forward(length)
        turtle.pendown()
    if number == 7:
        turtle.left(90)
        turtle.forward(length*1.5)
        turtle.right(135)
        turtle.forward(length*2)
        turtle.left(45)
    if number == 8:
        turtle.forward(length*2)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length*2)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
    if number == 9:
        turtle.left(90)
        turtle.backward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length*2.5)




def shift_vertical(len):
    turtle.penup()
    turtle.forward(len)
    turtle.pendown()




window = turtle.Screen()
window.title("Digital Digits")
turtle.speed(0)
turtle.penup()
turtle.setx(-150)
turtle.sety(+270)
turtle.pendown()
length = 10
turtle.right(90)

for i in range(10):
    print_digits(i,length)
    shift_vertical(length*2)



turtle.done()