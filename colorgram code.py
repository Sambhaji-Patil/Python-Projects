# import colorgram

# Extract 6 colors from an image.
# color_list = []
# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     color_list.append(new_colors)
# print(color_list)

import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.hideturtle()

color = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49),
         (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31),
         (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
         (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.penup()
for dots in range(1,number_of_dots+1):
    tim.pendown()
    tim.dot(20, random.choice(color))
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