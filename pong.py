import turtle

# Game Window
window = turtle.Screen()
window.title("Pong by Michael Molcsan")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


# Score
score_left = 0
score_right = 0


# Left Paddle
paddle_l = turtle.Turtle()
paddle_l.speed(0) 
paddle_l.shape("square")
paddle_l.color("green")
paddle_l.shapesize(stretch_wid=5, stretch_len=1)
paddle_l.penup()
paddle_l.goto(-350, 0)


# Right Paddle
paddle_r = turtle.Turtle()
paddle_r.speed(0) 
paddle_r.shape("square")
paddle_r.color("green")
paddle_r.shapesize(stretch_wid=5, stretch_len=1)
paddle_r.penup()
paddle_r.goto(350, 0)


# Ball 
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player Left: 0  Player Right: 0", align="center", font=("Courier", 24, "normal"))


# Right and Left Paddles Up and Down Motion
def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)

def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)

def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)

# Keyboard binding (W, S, Up Arrow, Down Arrow)
window.listen()
window.onkeypress(paddle_l_up, "w")
window.onkeypress(paddle_l_down, "s")
window.onkeypress(paddle_r_up, "Up")
window.onkeypress(paddle_r_down, "Down")


# Main game loop
while True:
    window.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        pen.clear()
        pen.write("Player Left: {}  Player Right: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))

    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        pen.clear()
        pen.write("Player Left: {}  Player Right: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() + 50 and ball.ycor() > paddle_r.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_l.ycor() + 40 and ball.ycor() > paddle_l.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
