# import colorgram
# colors = colorgram.extract("image.jpg", 30)
# rgbColors = []
# # rgb = first_color.rgb //from documentation
# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     newColor=(r,g,b)
#     rgbColors.append(newColor)
# print(rgbColors)


from turtle import *
import random

colormode(255)
tartar = Turtle()

colorList = [
    (202, 164, 109),
    (236, 239, 243),
    (153, 75, 49),
    (222, 201, 136),
    (53, 94, 124),
    (171, 153, 41),
    (136, 32, 21),
    (133, 163, 184),
    (197, 93, 73),
    (48, 123, 87),
    (73, 44, 36),
    (14, 97, 72),
    (145, 178, 148),
    (91, 73, 75),
    (233, 176, 165),
    (160, 143, 159),
    (54, 47, 50),
    (184, 205, 172),
    (35, 61, 75),
    (22, 85, 89),
    (146, 19, 21),
    (86, 146, 130),
    (38, 67, 91),
    (13, 72, 66),
    (106, 128, 155),
    (175, 99, 101),
    (176, 192, 209),
]

tartar.penup()
tartar.hideturtle()
tartar.setheading(225)
tartar.forward(300)
tartar.setheading(0)
numberOfdots = 100
tartar.speed("fastest")
for i in range(1, numberOfdots+1):
    tartar.dot(20, random.choice(colorList))
    tartar.forward(50)

    if i % 10 == 0:
        tartar.setheading(90)
        tartar.forward(50)
        tartar.setheading(180)
        tartar.forward(500)
        tartar.setheading(0)


screen = Screen()
screen.exitonclick()
