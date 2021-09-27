import turtle as t
import random
# import heroes
# import colors


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# print(heroes.gen())




# # Draw square
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# # Draw shapes
# for sides in range(3, 20):
#     tim.pencolor(random.choice(colors.colors))
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)

# # Random walk
# directions = [0, 90, 180, 270]
# tim.pensize(6)
# tim.speed(0)
# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# Spirograph
# tim.speed(0)
# for tiltangle in range(0, 360, 5):
#     tim.pencolor(random_color())
#     tim.setheading(tiltangle)
#     tim.circle(100)

# hirst painting
color_list = [(149, 75, 75), (222, 201, 201), (53, 93, 93), (170, 154, 154), (138, 31, 31), (134, 163, 163), (197, 92, 92), (47, 121, 121), (73, 43, 43),(145, 178, 178), (14, 98, 98), (232, 176, 176), (160, 142, 142), (54, 45, 45), (101, 75, 75), (183, 205, 205), (36, 60, 60), (19, 86, 86), (82, 148, 148), (147, 17, 17), (27, 68, 68), (12, 70, 70), (107, 127, 127), (176, 192, 192), (168, 99, 99)]
DIST = 50
RADIUS = 20

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.speed(0)
tim.hideturtle()

for y in range(-250, 250, DIST):
    for x in range(-250, 250, DIST):
        tim.goto(x, y)
        tim.dot(RADIUS, random.choice(color_list))



screen = t.Screen()
screen.exitonclick()
