#________________________________________Design 1 : Dot art_____________________________________________________
import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.hideturtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ran_col = (r, g, b)
    return ran_col

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.penup()
for dots in range(1,number_of_dots+1):
    tim.pendown()
    tim.dot(20,random_color())
    tim.penup()
    tim.forward(50)

    if dots % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = t.Screen()
screen.exitonclick()

#______________________________________________Design 2: Circle Design _____________________________________________________
import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.width(3)
tim.speed(0)
t.bgcolor("yellow")
t.title("Design Random")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ran_col = (r, g, b)
    return ran_col


gap = t.numinput("Gap Size" ,"Enter the gap required: ")
val = 10
for _ in range(int(360/gap)):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(val)
    val+=gap

screen.exitonclick()
