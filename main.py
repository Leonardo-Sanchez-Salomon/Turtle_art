from turtle import Turtle, Screen, colormode
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tim.pencolor(r, g, b)


tim = Turtle()
tim.shape("turtle")
tim.color("dark violet")
colormode(255)

# Code below draws shapes in a random color
# for num in range(3, 11): # from shape with 3 sides to shapes with 10
#     i = 0
#     random_color() #generates random pen color
#     while i < num:
#         side = 360 / num
#         tim.forward(100)
#         tim.right(side)
#         i += 1

# Code below randomly walks
# tim.pensize(10)   #changes pen size
# tim.speed(0)      #changes speed the turtle draws at
# true = True
# direction = [0, 90, 180, 270]
# while true:
#     random_color()
#     tim.setheading(random.choice(direction))
#     tim.forward(25)

# Code below will draw circles circularly
# tim.speed(0)
# start = 0
# while start <= 360:  # Stops when it's done a full circle
#     random_color()
#     tim.setheading(start)     # Shifts its position to a degree
#     tim.circle(100)
#     start += 5        # Adds to the degree to keep it moving


# Code below will import the colors used in a Hirst dot painting
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('Hirst_more_dots.jpg', 40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

# Using list created by previous code will be making a hurst dot painting
# color_list = [(254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40), (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112), (16, 54, 243), (240, 16, 16)]
#
# tim.penup()
# tim.setx(-250)
# y_position = -200
# while tim.position() != (250, 250):   # Stops when turtle reaches this position
#     tim.setx(-250)
#     tim.sety(y_position)
#     for num in range(0, 10):          # Does ten dots in each row
#         tim.dot(20, random.choice(color_list))
#         tim.forward(50)
#     print(tim.position())
#     y_position += 50
screen = Screen()
screen.exitonclick()

