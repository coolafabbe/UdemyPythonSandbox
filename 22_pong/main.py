import turtle as t
import paddle
import ball as b
import time


screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
ball = b.Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    ball.move()

    # detect collision with the wall.
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # detect collision with the right paddle.
    if ball.distance(r_paddle) < 50 and r_paddle.xcor() > 320 or ball.distance(l_paddle) < 50 and l_paddle.xcor() < -320:
        ball.bounce_x()

    # detect R paddle misses
    if ball.xcor() > 360:
        ball.reset_position()

    # detect L paddle misses
    if ball.xcor() < -360:
        ball.reset_position()

    screen.update()
    time.sleep(0.1)



screen.exitonclick()