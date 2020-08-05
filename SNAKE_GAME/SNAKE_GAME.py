 #####################!! PROGRAMMER : S.MUKILAN !!############################

#-------------------------------  SNAKE GAME --------------------------------#


import turtle
import random
import time
import winsound

score = 0
show_score = 0
snake_food = ['food_blade.gif','food_apple.gif']
sn_body = []

wn = turtle.Screen()
wn.title("SNAKE GAME BY MUKILAN")
winsound.PlaySound("music.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
wn.setup(width=800, height=550)
wn.bgpic('board_instruct.png')
wn.update()
time.sleep(4)
wn.bgpic('board_bg.png')
wn.tracer(0)
turtle.addshape('food_apple.gif')
turtle.addshape('food_blade.gif')



sn_head = turtle.Turtle()
sn_head.color('black')
sn_head.speed(0)
sn_head.shape("square")
sn_head.shapesize(stretch_wid=0.70,stretch_len=0.70)
sn_head.penup()
sn_head.goto(0,0)
sn_head.direction = 'stop'


food = turtle.Turtle()
food.shape(random.choice(snake_food))
food.shapesize(stretch_wid=0.55,stretch_len=0.55)
fn_x = random.randint(-330, 330)
fn_y = random.randint(-215, 215)
food.penup()
food.goto(fn_x , fn_y)


pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.ht()
pen.penup()
pen.goto(0, 235)
pen.write("SCORE:0",align="center", font=("courier", 18, "normal"))
pen.goto(0, -265)
pen.write("SNAKE GAME BY MUKILAN",align="center", font=("courier", 18, "bold"))


def sn_head_U():
    if sn_head != 'Down':
        sn_head.direction = 'Up'
        

def sn_head_D():
    if sn_head != 'Up':
        sn_head.direction = 'Down'


def sn_head_R():
    if sn_head != 'Left':
        sn_head.direction = 'Right'
       

def sn_head_L():
    if sn_head != 'Right':
        sn_head.direction = 'Left'


def sn_move():
    if sn_head.direction == 'Up':
        sn_y = sn_head.ycor()
        sn_head.sety(sn_y + 15)

    if sn_head.direction == 'Down':
        sn_y = sn_head.ycor()
        sn_head.sety(sn_y - 15)

    if sn_head.direction == 'Right':
        sn_x = sn_head.xcor()
        sn_head.setx(sn_x + 15)

    if sn_head.direction == 'Left':
        sn_x = sn_head.xcor()
        sn_head.setx(sn_x - 15)

def quit_game():
    time.sleep(2)
    turtle.bye()

wn.listen()
wn.onkeypress(sn_head_U, "Up")   
wn.onkeypress(sn_head_D, "Down")    
wn.onkeypress(sn_head_L, "Left")     
wn.onkeypress(sn_head_R, "Right")
wn.onkeypress(quit_game, "q")

while True:
    wn.update()

    if sn_head.distance(food) < 20:
        food.shape(random.choice(snake_food))
        time.sleep(0.01)
        fn_x = random.randint(-340, 340)
        fn_y = random.randint(-215, 215)
        
        food.goto(fn_x,fn_y)
        inc_score = random.randint(3, 6)
        show_score = show_score + inc_score
        pen.goto(0, 235)
        pen.color('red')
        pen.clear()
        pen.write("SCORE:{}".format(show_score),align="center", font=("courier", 18, "normal"))
        pen.goto(0, -265)
        pen.write("SNAKE GAME BY MUKILAN",align="center", font=("courier", 18, "bold"))            

      
        build_body = turtle.Turtle()
        build_body.speed(0)
        build_body.shape("square")
        build_body.shapesize(stretch_wid=0.70,stretch_len=0.70)
        build_body.color("green")
        build_body.penup()
        sn_body.append(build_body)


        
    for index in range(len(sn_body)-1, 0, -1):
        x = sn_body[index-1].xcor()
        y = sn_body[index-1].ycor()
        sn_body[index].goto(x, y)

    
    if len(sn_body) > 0:
        x = sn_head.xcor()
        y = sn_head.ycor()
        sn_body[0].goto(x,y)

    sn_move()

    for body in sn_body:
        if body.distance(sn_head) < 15:
            time.sleep(1)
            winsound.PlaySound("music.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
            sn_head.direction = 'stop'
            sn_head.goto(0,0)
            show_score = 0
            
            for body in sn_body:
                body.goto(1000,1000)
                
            sn_body.clear()
            pen.clear()
            pen.goto(0, 235)
            pen.write("SCORE:{}".format(show_score),align="center", font=("courier", 18, "normal"))
            pen.goto(0, 0)
            pen.write("SNAKE COLLIDE WITH BODY",align="center", font=("courier", 18, "bold"))
            time.sleep(2)
            pen.clear()
            pen.goto(0, 235)
            pen.write("SCORE:{}".format(show_score),align="center", font=("courier", 18, "normal"))

    if sn_head.xcor() < -365 or sn_head.xcor() > 365 or sn_head.ycor() < -240 or sn_head.ycor() > 240:
        time.sleep(1)
        winsound.PlaySound("music.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
        sn_head.direction = 'stop'
        sn_head.goto(0,0)
        show_score = 0
        
        
        for body in sn_body:
            body.goto(1000,1000)
            
        sn_body.clear()
        pen.clear()
        pen.goto(0, 235)
        pen.write("SCORE:{}".format(show_score),align="center", font=("courier", 18, "normal"))
        pen.goto(0, 0)
        pen.write("SNAKE COLLIDE WITH BORDER",align="center", font=("courier", 18, "bold"))
        time.sleep(2)
        pen.clear()
        pen.goto(0, 235)
        pen.write("SCORE:{}".format(show_score),align="center", font=("courier", 18, "normal"))
    time.sleep(0.1)
                


#-------------------------------  SNAKE GAME --------------------------------#
###########################!!! GAME COMPLECTED !!!############################
