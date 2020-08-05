                # $$$$$$$$$$ PROGRAMMER : MUKILAN.S $$$$$$$$$$$$ #

#------------------------------  TIC TAC TOE   -------------------------------#

import turtle           #TO CREATE ANNIMATION AND 2D GAMES
import time         #TO MANAGE AND ACCESS TIME
import winsound        #TO PLAY MUSICS ON BACKGROUND

#CREATING GAME SCREEN
wn = turtle.Screen()
wn.title("TIC_TAC_TOE GAME BY MUKILAN")

#PLAY BACKGROUND SOUND
winsound.PlaySound("bgmus.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

#SETTING THE SCREEN WIDTH AND HEIGHT
wn.setup(width=500, height=500)
wn.bgpic("x_o.png")     #TO TAKE PICTURE FOR BG
wn.update()
time.sleep(4)       #STOP EXECUTION OF PROGRAM
wn.bgpic("board.png")    
wn.update()     #UPDATING THE WINDOW

#THIS FOR WINS AND TURNS X_O
chance = 1
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0
b9 = 0

    
#PEN ATTRIBUTE TO WRITE ON SCREEN
pen = turtle.Turtle()
pen.color('black')      #COLOR OF THE PEN
pen.penup()
pen.ht()    #HIDE THE TURTLE
pen.goto(0, +210)
pen.write("X-O GAME",align="center",font=("courier",25,"bold"))
pen.penup()
pen.goto(0 ,-240)
pen.write("GAME DESIGNED BY MUKILAN",align="center",font=("courier",25,"bold"))
pen.goto(0, 170)

    
#MAIN FUNCTION
def pass_func(x,y):
    global chance
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    if x < -79 and y > 73:
        if chance%2 == 1:
            pen.goto(-140,50)
            pen.write("X",align="center",font=("courier",100,"normal"))
            b1 = "x"
        if chance%2 != 1:
            pen.goto(-140,50)
            pen.write("O",align="center",font=("courier",100,"normal"))
            b1 = "o"
        chance = chance + 1


    if x < -79 and y < 73 and y > -56:
        if chance%2 == 1:
            pen.goto(-140,-65)
            pen.write("X",align="center",font=("courier",100,"normal"))
            b4 = "x"
        if chance%2 != 1:
            pen.goto(-140,-65)
            pen.write("O",align="center",font=("courier",100,"normal"))
            b4 = "o"
        chance = chance + 1


    if x < -79 and y < -56:
        if chance%2 == 1:
            pen.goto(-140,-195)
            pen.write("X",align="center",font=("courier",100,"normal"))
            b7 = "x"
        if chance%2 != 1:
            pen.goto(-140,-195)
            pen.write("O",align="center",font=("courier",100,"normal"))
            b7 = "o"
        chance = chance + 1


    if x > -79 and y > 71 and x < 61:
        if chance%2 == 1:
            pen.goto(-15,50)
            pen.write("X",align="center",font=("courier",100,"normal"))
            b2 = "x"
        if chance%2 != 1:
            pen.goto(-15,50)
            pen.write("O",align="center",font=("courier",100,"normal"))
            b2 = "o"
        chance = chance + 1

    if x > -79 and y < 71 and x < 61 and y > -57:
        if chance%2 == 1:
            pen.goto(-5,-65)
            pen.write("X",align="center",font=("courier",100,"normal"))
            b5 = "x"
        if chance%2 != 1:
            pen.goto(-5,-65)
            pen.write("O",align="center",font=("courier",100,"normal"))
            b5 = "o"
        chance = chance + 1

    if x > -79 and x < 61 and y < -57:
        if chance%2 == 1:
            pen.goto(-15,-195)
            pen.write("X",align="center",font=("courier",100,"normal"))
            b8 = "x"
        if chance%2 != 1:
            pen.goto(-15,-195)
            pen.write("O",align="center",font=("courier",100,"normal"))
            b8 = "o"
        chance = chance + 1        


    if x > 60 and y > 70 :
        if chance%2 == 1:
            pen.goto(140,+50)
            pen.write("X",align="center",font=("courier",100,"normal"))
            b3 = "x"
        if chance%2 != 1:
            pen.goto(140,+50)
            pen.write("O",align="center",font=("courier",100,"normal"))
            b3 = "o"
        chance = chance + 1        

    if x > 60 and y > -57 and y < 68:
        if chance%2 == 1:
            pen.goto(140,-65)
            pen.write("X",align="center",font=("courier",100,"normal"))
            b6 = "x"
        if chance%2 != 1:
            pen.goto(140,-65)
            pen.write("O",align="center",font=("courier",100,"normal"))
            b6 = "o"
        chance = chance + 1        

    if x > 60 and y < -57 :
        if chance%2 == 1:
            pen.goto(140,-195)
            pen.write("X",align="center",font=("courier",100,"normal"))
            b9 = "x"
        if chance%2 != 1:
            pen.goto(140,-195)
            pen.write("O",align="center",font=("courier",100,"normal"))
            b9 = "o"
        chance = chance + 1

    if b1 == b4 == b7 == "x":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[X WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)       #TO PASS EXECUTION OF PROGRAM
        turtle.bye()    #CLOSE THE GAME SCREEN

    if b1 == b4 == b7 == "o":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[O WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)
        turtle.bye()

    if b2 == b5 == b8 == "x":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[X WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)
        turtle.bye()

    if b2 == b5 == b8 == "o":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[O WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)
        turtle.bye()

    if b3 == b6 == b9 == "x":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[X WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)       #TO PASS EXECUTION OF PROGRAM
        turtle.bye()    #CLOSE THE GAME SCREEN

    if b3 == b6 == b9 == "o":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[O WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)
        turtle.bye()

    if b1 == b2 == b3 == "x":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[X WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)
        turtle.bye()

    if b1 == b2 == b3 == "o":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[O WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)
        turtle.bye()

    if b4 == b5 == b6 == "x":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[X WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)       #TO PASS EXECUTION OF PROGRAM
        turtle.bye()    #CLOSE THE GAME SCREEN
        
    if b4 == b5 == b6 == "o":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[O WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)
        turtle.bye()

    if b7 == b8 == b9 == "x":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[X WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)
        turtle.bye()

    if b7 == b8 == b9 == "o":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[O WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)       #TO PASS EXECUTION OF PROGRAM
        turtle.bye()    #CLOSE THE GAME SCREEN
        
    if b3 == b5 == b7 == "x":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[X WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)
        turtle.bye()

    if b3 == b5 == b7 == "o":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[O WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)
        turtle.bye()

    if b1 == b5 == b9 == "x":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[X WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)       #TO PASS EXECUTION OF PROGRAM
        turtle.bye()    #CLOSE THE GAME SCREEN

    if b1 == b5 == b9 == "o":
        pen.goto(0, 0)
        pen.color("red")
        pen.write("[O WINS]",align="center",font=("courier",70,"bold"))
        time.sleep(3)
        turtle.bye()
                
wn.onscreenclick(pass_func)     #THIS TO GET THE CLICKED X AND Y CORDINATE


            # $$$$$$$$$$ PROGRAMMER : MUKILAN.S $$$$$$$$$$$$ #
            # $$$$ PROGRAMM COMPLECTED ENJOY THE GAME $$$$ #



