from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.title("P0NG")
screen.bgcolor("black")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()


screen.listen()


screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.ontimer(ball.move_it, 100)
    screen.update()
    ball.move_it()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        # Ball bounce

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R Paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L Paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()