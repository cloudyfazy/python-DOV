#imports
import turtle
import math
import random






#screen
wn = turtle.Screen()
wn.bgcolor('green')
wn.bgpic("kbgame-bg.gif")
wn.tracer(3)

#border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()             

#creating the turtle

player = turtle.Turtle()
player.color("red")
player.shape("circle")
player.penup()
player.speed(0)

#score

score = 0



#create multiple goals
maxGoals = 6
goals= []

for count in range (maxGoals):
 goals.append(turtle.Turtle())
 goals[count].color("white")
 goals[count].shape("triangle")
 goals[count].penup()
 goals[count].speed(0)
 goals[count].setposition(random.randint(-300, 300), random.randint(-300,300))




#speed
speed = 1

#functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False 



#set keyboard bindings
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")

while True:
    player.forward(speed)


#boundary checking
    if player.xcor() > 300 or player.xcor() < -300:
       player.right(180)

    if player.ycor() > 300 or player.ycor() < -300:
       player.right(180)

       #collision 
   
        #move goal
    for count in range(maxGoals):
        goals[count].forward(3)

        #boundary checking
        if goals[count].xcor() > 280 or goals[count].xcor() < -280:
           player.right(180)

        if goals[count].ycor() > 280 or goals[count].ycor() < -280:
          goals[count].right(180)

        #collision checking

        if isCollision(player, goals[count]):
          goals[count].setposition(random.randint(-300,300), random.randint(-300,300))
          goals[count].right(random.randint(0,360))
          score += 1

          #draw score on screen
          mypen.undo()
          mypen.penup()
          mypen.hideturtle()
          mypen.setposition(-290, 310)
          scorestring = "Score:%s" %score
          mypen.write(scorestring, False, Align="left", Font=("Arial",14,"normal"))          

        delay = input("press enter to finish")






