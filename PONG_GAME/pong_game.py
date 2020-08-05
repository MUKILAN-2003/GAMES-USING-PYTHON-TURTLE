                # $$$$$$$$$$ PROGRAMMER : MUKILAN.S $$$$$$$$$$$$ #
                   
#-----------------------------     PONG GAME     -----------------------------#
 
import turtle       #MODULE TO CREATE GAME OR ANNIMATION
import time     #MODULE TO TIME MANAGEMENT
import os           #MODULE TO ACCESS THE OPERATING SYSTEM
import winsound         #MODULE TO PLAY SOUND

wn = turtle.Screen()
wn.title("PONG GAME BY MUKILAN")        #TITLE OF THE GAME WINDOW
wn.bgpic("pongintro.png")
wn.update()
time.sleep(4)           #THIS STOP EXECTION OF PROGRAMM FOR GIVEN TIME
wn.bgpic("intropong.png")
wn.update()     #UPDATE THE WINDOW
time.sleep(4)
wn.bgpic("py.png")
wn.setup(width=730, height=600) #SETING SCREEN SIZE
winsound.PlaySound("bgmus2.wav", winsound.SND_ASYNC | winsound.SND_ALIAS) #PLAY BACKGROUND SOUND
time.sleep(1)
wn.tracer(0)

#SCORE OF THE PLAYER
score_a = 0
score_b = 0

#RIGHT SIDE PADDLE
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("red")           #YOU CAN GIVE ANY OTHER COLOR
paddle_b.shape("square")        #YOU CAN GIVE ANY OTHER SHAPE
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#LEFT SIDE PADDLE
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("red")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=1,stretch_len=5)
paddle_a.penup()
paddle_a.left(90)
paddle_a.goto(-350, 0)

#BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")        #YOU CAN GIVE ANY OTHER SHAPE
ball.color("black")         #YOU CAN GIVE ANY OTHER COLOR
ball.penup()
ball.goto(0, 0)
ball.dx = + 1.2
ball.dy = - 1.2

#PEN ATTRIBUTE TO WRITE ON SCREEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("MANOJ: SCORE     MUKILAN: SCORE",align="center", font=("courier", 16, "normal"))
#YOU CAN CHANGE NAME OF PLAYER IN UP LINE
pen.goto(-330 ,-260)
pen.write("PRESS Q FOR EXIT",align="left", font=("courier", 9, "normal"))



#IT WILL SHOW CREDITS
def show_cred():
    pen.goto(0, 0)
    pen.color("red")
    pen.write("GAME OVER", align="center", font=("courier", 50, "normal"))
    pen.goto(0, -260)
    pen.write("PROGRAMMED BY MUKILAN",align="center", font=("courier", 34, "normal"))
    time.sleep(3)
    turtle.bye()        #TO CLOSE THE GAME WINDOW
    pen.clear()


#FUNCTION TO MOVE UP THE RIGHT PADDLE
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

#FUNCTION TO MOVE DOWN THE RIGHT PADDLE
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#FUNCTION TO MOVE UP THE LEFT PADDLE
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

#FUNCTION TO MOVE DOWN THE LEFT PADDLE
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


#TO SHOW THE INSTRUCTION
def show_inst():
    wn.bgpic("intropong.png")
    wn.update()
    time.sleep(3)
    wn.bgpic("py.png")
    

#TO LISTEN THE WINDOWN    
wn.listen()
wn.onkeypress(paddle_b_up, "Up")   #TO MOVE THE RIGHT PADDLE UP
wn.onkeypress(paddle_b_down, "Down")    #TO MOVE THE RIGHT PADDLE DOWN
wn.onkeypress(paddle_a_up, "w")     #TO MOVE THE LEFT PADDLE UP
wn.onkeypress(paddle_a_down, "s")   #TO MOVE THE LEFT PADDLE DOWN
wn.onkeypress(show_cred, "q")       #TO EXIT FROM THE GAME
wn.onkeypress(show_inst, "i")       #TO SHOW INSTRUCTION



while True:         #MAIN LOOP
    wn.update()         #UPDATE THE WINDOW OFTEN

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
#TOP BODDER BOUNCE
    if ball.ycor() > 290:
        ball.sety(290)      
        ball.dy *= - 1

#BOTTOM BODDER BOUNCE       
    if ball.ycor() < -290:
        ball.sety(-290)     
        ball.dy *= - 1

#RIGHT SIDE PLAYER MISS THE BALL POINT INCREASE TO LEFT SIDE PLAYER        
    if ball.xcor() > 390:
        ball.goto(0, 0)     
        ball.dx *= -1
        score_a += 1
        pen.goto(0, 260)
        pen.clear()
        pen.write("MANOJ: {}      MUKILAN: {}".format(score_a, score_b),align="center", font=("courier", 18, "normal"))

    #IF THE LEFT PLAYER GET 10 POINTS HE WINS
    if score_a == 10:
        pen.goto(0, 0)          #THIS TO PRINT THE WORD IN CENTER
        pen.color("black")
        pen.write("MANOJ WINS",align="center", font=("courier", 40, "normal"))
        time.sleep(2.5)
        turtle.bye()

#LEFT SIDE PLAYER MISS THE BALL POINT INCREASE TO RIGHT SIDE PLAYER
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= - 1
        score_b += 1
        pen.goto(0, 260)
        pen.clear()
        pen.write("MANOJ: {}      MUKILAN: {}".format(score_a, score_b),align="center", font=("courier", 18, "normal"))

    #IF THE RIGHT PLAYER GET 10 POINTS HE WINS
    if score_b == 10:
        pen.goto(0, 0)      #THIS TO PRINT THE WORD IN CENTER
        pen.color("black")
        pen.write("MUKILAN WINS",align="center", font=("courier", 40, "normal"))
        time.sleep(2.5)
        turtle.bye()


#BALL HITS THE PADDLE RIGHT
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):        
        ball.setx(340)
        ball.dx  *= -1
        
#BAL HITS THE PADDLE LEFT
    if (ball.xcor() < -340 and ball.xcor() < 350) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40):        
        ball.setx(-340)
        ball.dx  *= -1
#CHECKS THE PADDLE
    if (paddle_a.ycor() < -300):
        paddle_a.goto(-350,-300)

    if (paddle_b.ycor() > 300):
        paddle_b.goto(350,300)

    if (paddle_a.ycor() > +300):
        paddle_a.goto(-350,300)

    if (paddle_b.ycor() < -300):
        paddle_b.goto(350,-300)     
        

            # $$$$$$$$$$ PROGRAMMER : MUKILAN.S $$$$$$$$$$$$ #
            # $$$$ PROGRAMM COMPLECTED ENJOY THE GAME $$$$ #

            

     
