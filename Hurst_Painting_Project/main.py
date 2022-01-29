# import colorgram

# colors = colorgram.extract('image.jpg', 40)
# rgb_color = []
# for color in colors:
#     r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
#     rgb_color.append(((r, g, b)))
#
# print(rgb_color)
import turtle
import random
from turtle import Turtle, Screen

hurst = Turtle()
turtle.colormode(255)
hurst.speed(0)

color_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63),
              (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20),
              (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217),
              (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178), (252, 197, 0),
              (29, 84, 92), (228, 174, 166), (186, 190, 201), (73, 73, 39)]
x_value = 0.00
y_value = 0.00
hurst.penup()
hurst.hideturtle()
for _ in range(100):
    hurst.dot(20, random.choice(color_list))
    hurst.forward(50)
    if hurst.pos() == (x_value+500,y_value):
        y_value += 40
        hurst.setposition(0.00, y_value)










screen = Screen()
screen.exitonclick()
