# PONG GAME
# python 3.9 - 01/06/2021
# By Tampella Giacomo - credits to @TokyioEdTech

import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @TampellaGiacomo")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# SCORE
score_a = 0
score_b = 0

# PADDLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# BALL 1
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("circle")
ball1.color("red")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 0.065
ball1.dy = -0.065

# BALL 2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("blue")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -0.085
ball2.dy = -0.085

# PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))

# FUNCTION
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# PLAY SOUND
def play_sound(sound_file, time = 0):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)

# KEYBOARD BINDING
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# MAIN GAME LOOP
while True:
    wn.update()

    # MOVE THE BALLS
    ball1.setx(ball1.xcor() + ball1.dx)
    ball1.sety(ball1.ycor() + ball1.dy)

    ball2.setx(ball2.xcor() + ball2.dx)
    ball2.sety(ball2.ycor() + ball2.dy)

    # BORDER CHECKING
    if ball1.ycor() > 290:
        ball1.sety(290)
        ball1.dy *= -1
        play_sound("bounce.mp3")

    if ball1.ycor() < -290:
        ball1.sety(-290)
        ball1.dy *= -1
        play_sound("bounce.mp3")

    if ball1.xcor() > 390:
        ball1.goto(0, 0)
        ball1.dx *=-1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    if ball1.xcor() < -390:
        ball1.goto(0, 0)
        ball1.dx *=-1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    if ball2.ycor() > 290:
        ball2.sety(290)
        ball2.dy *= -1
        play_sound("bounce.mp3")

    if ball2.ycor() < -290:
        ball2.sety(-290)
        ball2.dy *= -1
        play_sound("bounce.mp3")

    if ball2.xcor() > 390:
        ball2.goto(0, 0)
        ball2.dx *=-1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    if ball2.xcor() < -390:
        ball2.goto(0, 0)
        ball2.dx *=-1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    # PADDLE AND BALL COLLISION
    if (ball1.xcor() > 340 and  ball1.xcor() < 350) and (ball1.ycor() < paddle_b.ycor() + 40 and ball1.ycor() > paddle_b.ycor() -50):
            ball1.setx(340)
            ball1.dx *= -1
            play_sound("bounce.mp3")

    if (ball1.xcor() < -340 and  ball1.xcor() > -350) and (ball1.ycor() < paddle_a.ycor() + 40 and ball1.ycor() > paddle_a.ycor() -50):
            ball1.setx(-340)
            ball1.dx *= -1
            play_sound("bounce.mp3")

    if (ball2.xcor() > 340 and  ball2.xcor() < 350) and (ball2.ycor() < paddle_b.ycor() + 40 and ball2.ycor() > paddle_b.ycor() -50):
            ball2.setx(340)
            ball2.dx *= -1
            play_sound("bounce.mp3")

    if (ball2.xcor() < -340 and  ball2.xcor() > -350) and (ball2.ycor() < paddle_a.ycor() + 40 and ball2.ycor() > paddle_a.ycor() -50):
            ball2.setx(-340)
            ball2.dx *= -1
            play_sound("bounce.mp3")


    # AI PLAYER
    if ball1.xcor() > ball2.xcor():
        if paddle_b.ycor() < ball1.ycor() and abs(paddle_b.ycor() - ball1.ycor()) > 10:
            paddle_b_up()

        elif paddle_b.ycor() > ball1.ycor() and abs(paddle_b.ycor() - ball1.ycor()) > 10:
            paddle_b_down()
    else:
        if paddle_b.ycor() < ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
            paddle_b_up()

        elif paddle_b.ycor() > ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
            paddle_b_down()
