from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍Snake!🐍")
screen.tracer(0) 

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.check_collision(food, "head"):
        while snake.check_collision(food, "all"):
            food.refresh()
        scoreboard.increase_score()
        snake.create_segment("new")

    # detect collision with self or walls
    if snake.check_collision(snake.head, "all") or snake.check_walls():
        game_over = True
        scoreboard.game_over()

screen.exitonclick()