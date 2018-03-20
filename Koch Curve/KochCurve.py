#turtle standard graphics library for python
import turtle

#function to create koch snowflake or koch curve


def snowflake(lengthSide, level):
    if level == 0:
        turtle.forward(lengthSide)
        return
    lengthSide /= 3.0
    turtle.pencolor('#5e085e')
    snowflake(lengthSide,level-1)
    turtle.left(60)
    turtle.pencolor('#ff3300')
    snowflake(lengthSide, level-1)
    turtle.right(120)
    turtle.pencolor('#0d590d')
    snowflake(lengthSide, level - 1)
    turtle.left(60)
    turtle.pencolor('#5e085e')
    snowflake(lengthSide, level - 1)


# main function

# if __name__ ="__main__":

window = turtle.Screen()
window.title("Koch curve - Snowflake")
turtle.speed(0)
turtle.penup()
turtle.setx(-150)
turtle.sety(+150)
turtle.pendown()
length = 450.0

for i in range(3):
    snowflake(length,4)
    turtle.right(120)
 #   mainloop()




turtle.done()



""""Algorithm:


1. Make equilateral triangle  : side 300
2. for loop x3
        make a side forward recursively;
        turn right
3.  making a side forward recursively:
        get length 300
        300/3 = 100
        




"""