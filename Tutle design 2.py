from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500 , height=400)

game_on = False
user_bet = screen.textinput("Choice","Choose your Turtle's Colour")
color_list = ["red","green","blue","pink","orange","yellow"]
all_turtles = []

y = -125
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[i])
    new_turtle.penup()
    new_turtle.goto(-230,y)
    all_turtles.append(new_turtle)
    y+=50

if user_bet:
    game_on = True

while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                turtle.penup()
                turtle.goto(0, 0)
                turtle.pendown()
                # Write the statement on the screen
                turtle.write(f"You Win!! The {winning_color} turtle has won the game.", font=("Arial", 16, "normal"), align = "center")
            else:
                turtle.penup()
                turtle.goto(0, 0)
                turtle.pendown()
                # Write the statement on the screen
                turtle.write(f"You Lose!! The {winning_color} turtle has won the game.", font=("Arial", 16, "normal"), align = "center")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
    

screen.exitonclick()