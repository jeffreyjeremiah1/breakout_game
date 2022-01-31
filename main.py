from turtle import Screen, Turtle
import time
from obstacles import Blocks

# screen is made
screen = Screen()
screen.title = "Breakout game"
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# paddle is made
paddle = Turtle()
paddle.shape("square")
paddle.color("purple")
paddle.shapesize(stretch_wid=1, stretch_len=10)
paddle.penup()
paddle.goto(0, -240)

# ball is made
ball = Turtle()
ball.shape("circle")
ball.penup()
ball.color("white")
ball.goto(0, 0)
x_move = 1
y_move = 1

# score board is made
points = 0
score = Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write(f"Score: {points}", align="center", font=("serif", 24, "bold"))

# list of colors for block
colors = ["blue", "green", "red", "yellow"]
block_list = []
x_pos = -335
y_pos = 50

# display blocks on screen
for color in colors:
    for num in range(0, 7):
        block = Blocks(color=color, position=(x_pos, y_pos))
        block_list.append(block)
        x_pos += 110
    y_pos += 50
    x_pos = -335


# movement of paddles
def move_left():
    new_x = paddle.xcor() - 20
    paddle.goto(new_x, paddle.ycor())


def move_right():
    new_x = paddle.xcor() + 20
    paddle.goto(new_x, paddle.ycor())


def move_ball():
    new_x = ball.xcor() + x_move
    new_y = ball.ycor() - y_move
    ball.goto(new_x, new_y)


# ball deflects on wall
def bounce_wall():
    global x_move
    x_move *= -1


# ball deflects on paddle
def bounce_paddle():
    global y_move
    y_move *= -1


# updates score
def increase_score():
    global points, x_move, y_move
    points += 1
    score.clear()
    score.write(f"Score: {points}", align="center", font=("serif", 24, "bold"))
    if points > 10:
        x_move = 1.4
        y_move = 1.4
    if points > 20:
        x_move = 1.8
        y_move = 1.8



# listen to keys pressed
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.005)
    move_ball()
    screen.update()

    # detect contact between ball and side walls
    if ball.xcor() > 380 or ball.xcor() < -390:
        bounce_wall()

    # detect contact between ball and paddle
    if ball.distance(paddle) < 100 and ball.ycor() < -220 or ball.ycor() > 290:
        bounce_paddle()

    # display all blocks in list and detect contact with ball
    for block in block_list:
        if block.distance(ball) < 60 and ball.ycor() > 20:
            bounce_paddle()
            increase_score()
            block.hideturtle()
            x_axis_difference = ball.distance(block)
            y_axis_difference = ball.distance(block)

            block_list.remove(block)

    # detect when paddle mis ball
    if ball.ycor() < - 270 or not block_list:
        game_is_on = False

screen.exitonclick()
