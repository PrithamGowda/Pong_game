from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen =Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle=Paddle(370,0)
l_paddle=Paddle(-370,0)
ball=Ball()
score_board=Scoreboard()






screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on =True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.wall_bounce()

    #Detect collosion with paddle
    if ball.distance(r_paddle)<40 and ball.xcor() >320 or ball.distance(l_paddle)<40 and ball.ycor() >-320 :
        ball.paddle_bounce()
        ball.speed(7)


    #Detect paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        score_board.l_point()


    if ball.xcor()<-380:
        ball.reset_position()
        score_board.r_point()





screen.exitonclick()