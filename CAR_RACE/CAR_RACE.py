 #####################!! PROGRAMMER : S.MUKILAN !!############################

#--------------------------------  CAR_DASH ----------------------------------#


import turtle    #IMPORTING TURTLE MODULE
import time
import os
import random
import winsound

road_l = []     # ROAD STRIP
road_r = []
score = 0   #SCORE

turtle.addshape("obstacles.gif")
turtle.addshape("yellow_car.gif")         # CARS IMAGES ADDING TO TURTLE SHAPE
turtle.addshape("green_car.gif")
turtle.addshape("race_red.gif")
turtle.addshape('red_car.gif')
turtle.addshape('white_car.gif')
turtle.addshape('mustang_green_car.gif')
turtle.addshape('small_yellow_car.gif')      # CARS IMAGES ADDING TO TURTLE SHAPE
turtle.addshape('truck.gif')
turtle.addshape('blue_truck.gif')
turtle.addshape('yellow_truck.gif')

wn = turtle.Screen()
wn.setup(width=460, height=650)     #SETTING SCREEN SIZE
wn.title("CAR_RACE")    #SCREEN TITLE
wn.bgpic('INTRO.png')
wn.update()
wn.bgpic('INTRO.png')
time.sleep(5)
wn.bgpic('bg_race.png')     #BG PIC
wn.tracer(0)    #STOP THE WINDOW TO UPDATE

winsound.PlaySound("happy.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
#TO PLAY BACKGROUND MUSIC


pen = turtle.Turtle()
pen.ht()                #PEN TO WRITE ANY ON SCREEN
pen.speed(0)
pen.color('red')
pen.penup()

for i in range(3):
    #DRAW ROAD STRIP
    road_strip = turtle.Turtle()
    road_strip.shape('square')
    road_strip.shapesize(stretch_wid=5,stretch_len=0.7)
    road_strip.color('white')
    road_strip.penup()
    road = road_strip
    road_r.append(road)

    road_strip1 = turtle.Turtle()
    road_strip1.shape('square')
    road_strip1.shapesize(stretch_wid=5,stretch_len=0.7)
    road_strip1.color('white')
    road_strip1.penup()
    road= road_strip1
    road_l.append(road)
    
x_cor =  76
#PLACE ROAD STRIPS
road_r[0].goto(x_cor,205)
road_r[1].goto(x_cor,30)
road_r[2].goto(x_cor,-205)

road_l[0].goto(-x_cor,205)
road_l[1].goto(-x_cor,30)
road_l[2].goto(-x_cor,-205)
    
opp_path = [-150,0,150]     #OPP COMING VECHICLE PATH
opp = ['mustang_green_car.gif','small_yellow_car.gif',"obstacles.gif","green_car.gif","yellow_car.gif","race_red.gif","white_car.gif"]
opp_truck = ['truck.gif','blue_truck.gif','yellow_truck.gif']


#OPPOSITE VECHICLE 1
obstacles = turtle.Turtle()
obstacles.speed(0)
obstacles.shape(random.choice(opp))
obstacles.penup()
obstacles.goto(random.choice(opp_path),-70)

#OPPOSITE VECHICLE 2
driver1 = turtle.Turtle()
driver1.speed(0)
driver1.shape(random.choice(opp))
driver1.penup()
driver1.goto(random.choice(opp_path),230)

#OPPOSITE TRUCK
truck = turtle.Turtle()
truck.speed(0)
truck.shape(random.choice(opp_truck))
truck.penup()
truck.goto(random.choice(opp_path),230)

#PLAYER CAR
user_driver = turtle.Turtle()
user_driver.speed(0)
user_driver.shape('red_car.gif')
user_driver.penup()
user_driver.goto(0,-230)

#PLAYER CAR TO MOVE LEFT
def user_driver_l():
    x = user_driver.xcor()
    user_driver.setx(x - 150)

#PLAYER CAR TO MOVE LEFT     
def user_driver_r():
    x = user_driver.xcor()
    user_driver.setx(x + 150)
    
def move_white_strip():         #TO MOVE ROAD STRIP
    for i in range(3):    
        road_l[i].sety(road_l[i].ycor() - 5) 
        road_r[i].sety(road_r[i].ycor() - 5)
        if road_l[i].ycor() <= -314 or road_r[i].ycor() <= -314:
            road_l[i].goto(-x_cor, 240)
            road_r[i].goto(x_cor, 240)
    
def opp_move():             #OPPOSITE CAR TO MOVE
    y = driver1.ycor()
    driver1.sety(y - 4)

    if driver1.ycor() < -314:
        driver1.goto(random.choice(opp_path),250)
        driver1.shape(random.choice(opp))
        
    y = obstacles.ycor()                    
    obstacles.sety(y - 4)               #OPPOSITE CAR TO MOVE   

    if obstacles.ycor() < -314:
        obstacles.goto(random.choice(opp_path),250)
        obstacles.shape(random.choice(opp))

    y = truck.ycor()
    truck.sety(y - 4)    

    if truck.ycor() < -314:
        truck.goto(random.choice(opp_path),250)
        truck.shape(random.choice(opp_truck))

def border_check():     #PLAYER CAR BORDER VHECK
    if user_driver.xcor() > 150:
        user_driver.goto(150,-230)

    if user_driver.xcor() < -150:
        user_driver.goto(-150,-230)

def driven():           #TO SHOW DRIVEN DISTANCE
    if user_driver.xcor() < 300:
        global score
        pen.goto(0, 270)
        pen.clear()
        pen.write("DISTANCE DRIVEN:{}[meter]".format(score),align='center',font=('courier',17,'bold'))
        score = score + 1

wn.listen()             #LISTEN THE KEYBORD FOR KEY PRESS
wn.onkeypress(user_driver_l,'Left')
wn.onkeypress(user_driver_r,'Right')
    
game_over = False       #IF GAME OVER IS TRUE THE LOOP STOPS

while not game_over:            
    wn.update()     #TO UPDATE THE WINDOM
    time.sleep(0.01)

    border_check()

    opp_move()              

    driven()
    
    move_white_strip()


    #CHECK THE CAR CARACH 
    if user_driver.distance(driver1) < 80 or user_driver.distance(obstacles) < 80 or user_driver.distance(truck) < 110:
        pen.goto(0, 60)
        pen.write("CRACHED",align='center',font = ('courier',70,'bold'))
        pen.goto(0, 0)
        pen.write("DISTANCE DRIVEN:{} METER".format(score),align='center',font=('courier',21,'bold'))
        time.sleep(1.5)
        pen.goto(0, -70)
        pen.write("GAME DESIGNED BY MUKILAN",align='center',font=('courier',21,'bold'))
        time.sleep(4)
        game_over= True

turtle.bye()            #TO QUIT THE GAME WINDOW 

