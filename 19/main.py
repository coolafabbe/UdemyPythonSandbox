from turtle import Turtle, Screen, color

# # Etch-a-sketch
# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def turn_clockwise():
#     tim.right(5)

# def turn_counterclockwise():
#     tim.left(5)

# def clear():
#     tim.clear()
#     tim.goto(0,0)

# screen.listen()
# screen.onkey(key = "w", fun=move_forwards)
# screen.onkey(key = "s", fun=move_backwards)
# screen.onkey(key = "a", fun=turn_counterclockwise)
# screen.onkey(key = "d", fun=turn_clockwise)
# screen.onkey(key = "c", fun=clear)


# screen.exitonclick()
import random

# Turtle race
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color:\n({colors[0]}, {colors[1]}, {colors[2]}, {colors[3]}, {colors[4]}, {colors[5]})").lower()
if not user_bet in colors:
    print(f"{user_bet} is not a valid choice.")
    quit()

all_turtles = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[index])

    all_turtles.append(new_turtle)

if user_bet in colors:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            is_race_on = False

            if winning_color == user_bet:
                print("You won!")
            else:
                print("You lose! winning turtle was " + winning_color)

        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()