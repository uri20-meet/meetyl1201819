#JUST CHECKING STUFF

import turtle
from turtle import Turtle
import math
import random
import time

turtle.tracer(0)

SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_width()/2
RUNNING = True
SLEEP = 0.0077
class Ball(Turtle):
	def __init__(self, x, y, radius, dx, dy, color):
		Turtle.__init__(self)
		self.penup()
		self.goto(x, y)
		self.pendown()
		self.shape("circle")
		self.color(color)
		self.radius = radius
		self.shapesize(radius/10)
		self.dx = dx
		self.dy = dy

	def move(self):
		global SCREEN_WIDTH, SCREEN_HEIGHT
		self.penup()
		oldX = self.xcor()
		oldY = self.ycor()
		newX = oldX + self.dx
		newY = oldY + self.dy
		absX = math.fabs(newX)
		absY = math.fabs(newY)

		if absX >= SCREEN_WIDTH:
			self.dx = -self.dx
		if absY >= SCREEN_HEIGHT:
			self.dy = -self.dy

		self.goto(newX, newY)
		
		collisionInList(ballsList)

	def changeSize(self, addition):
		if (self.radius + addition)/10 >= 5:
			self.radius += addition
			self.shapesize(self.radius/10)


#_______________________________________________________________________________


numberOfBalls = 6
minimumRadius = 10
maximumRadius = 100
minimumDx = -5
maximumDx = 5
minimumDy = -5
maximumDy = 5
ballsList = []

for i in range(0,numberOfBalls):
	newBallX = random.randint(-SCREEN_WIDTH + maximumRadius, SCREEN_WIDTH - maximumRadius)
	newBallY = random.randint(-SCREEN_HEIGHT + maximumRadius, SCREEN_HEIGHT - maximumRadius)
	newBallRadius = random.randint(minimumRadius, maximumRadius)
	while newBallDx == 0 or newBallDy == 0:
		newBallDx = random.randint(minimumDx, maximumDx)
		newBallDy = random.randint(minimumDy, maximumDy)
	newBallColor = (random.random(),random.random(),random.random())
	myBall = Ball(newBallX, newBallY, newBallRadius, newBallDx, newBallDy, newBallColor)
	ballsList.append(myBall)

















def check_collision(ballA, ballB):
	global bgIsBlack
	xA = ballA.xcor()
	xB = ballB.xcor()
	yA = ballA.ycor()
	yB = ballB.ycor()
	distance = math.sqrt(math.pow((xB-xA),2) + math.pow((yB-yA),2))
	radiusA = ballA.radius
	radiusB = ballB.radius
	colorsList = ["blue" , "red", "black", "green", "yellow", "orange", "gray", "pink", "indigo"]
	if radiusA + radiusB >= distance:
		if radiusA < radiusB:
			newX = random.randint(-450, 450)
			newY = random.randint(-350, 350)
			newColor = random.randint(0, 8)
			newSize = random.randint(-3, 4)
			ballA.goto(newX, newY)
			ballA.changeSize(newSize)
			ballA.color(colorsList[newColor])
			ballB.changeSize(5)

		elif radiusA > radiusB:
			newX = random.randint(-150, 150)
			newY = random.randint(-150, 150)
			newColor = random.randint(0, 8)
			newSize = random.randint(-10, 10)
			ballB.goto(newX, newY)
			ballB.changeSize(newSize)
			ballB.color(colorsList[newColor])
			ballA.changeSize(10)
		return(True)
	else:
		return(False)

def collisionInList(listOfBalls):
	collided = False
	for i in range(0,len(listOfBalls)):
		for q in range(i+1,len(listOfBalls)):
			if check_collision(listOfBalls[i], listOfBalls[q]) and listOfBalls[i] !=listOfBalls[q] :
				collided = True

#______________________________________________________________________________


bob = Ball(100, 0, 48, 0.1, 0.01, "green")
john = Ball(100, 250, 32, -0.15, 0.06, "blue")
kevin = Ball(-100, 0, 40, 0.07, 0.16, "red")
arl = Ball(0, -300, 36, 0.18, -0.07, "yellow")
shawn = Ball(-200, -100, 20, -0.09, -0.11, "orange")
myBall = Ball(-300, -300, 35, -0.09, -0.11, "indigo")
while True:
	bob.move()
	john.move()
	kevin.move()
	arl.move()
	shawn.move()
	myBall.move()
	turtle.update()