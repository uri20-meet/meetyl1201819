import turtle
from turtle import Turtle
import math
import random
#import time

turtle.tracer(0)

SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
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


	def addToSize(self, addition):
		
		self.radius += addition
		self.shapesize(self.radius/10)

	def changeSize(self, newSize):
		
		self.radius = newSize
		self.shapesize(self.radius/10)

#_______________________________________________________________________________

def moveAllBalls(allBalls):
	for i in allBalls:
		i.move()
#_______________________________________________________________________________

numberOfBalls = 9
minimumRadius = 10
maximumRadius = 30
minimumDx = -0.4
maximumDx = 0.4
minimumDy = -0.4
maximumDy = 0.4
ballsList = []


def check_collision(ballA, ballB):
	xA = ballA.xcor()
	xB = ballB.xcor()
	yA = ballA.ycor()
	yB = ballB.ycor()
	distance = math.sqrt(math.pow((xB-xA),2) + math.pow((yB-yA),2))
	radiusA = ballA.radius
	radiusB = ballB.radius
	if radiusA + radiusB >= distance:

		if radiusA < radiusB:
			newX = random.randint(-SCREEN_WIDTH + maximumRadius, SCREEN_WIDTH - maximumRadius)
			newY = random.randint(-SCREEN_HEIGHT + maximumRadius, SCREEN_HEIGHT - maximumRadius)
			newSize = random.randint(minimumRadius, maximumRadius)
			ballA.goto(newX, newY)
			ballA.changeSize(newSize)
			ballA.color(random.random(),random.random(),random.random())
			ballB.addToSize(10)

		elif radiusA > radiusB:
			newX = random.randint(-SCREEN_WIDTH + maximumRadius, SCREEN_WIDTH - maximumRadius)
			newY = random.randint(-SCREEN_HEIGHT + maximumRadius, SCREEN_HEIGHT - maximumRadius)
			newSize = random.randint(minimumRadius, maximumRadius)
			ballB.goto(newX, newY)
			ballB.changeSize(newSize)
			ballB.color(random.random(),random.random(),random.random())
			ballA.addToSize(10)

		return(True)
	else:
		return(False)

def collisionInList(listOfBalls):
	collided = False
	for i in range(0,len(listOfBalls)):
		for q in range(i+1,len(listOfBalls)):
			if check_collision(listOfBalls[i], listOfBalls[q]) and listOfBalls[i] !=listOfBalls[q] :
				collided = True

def check_myball_collision():
	for i in range(0,len(ballsList)):
		xA = myBall.xcor()
		xB = ballsList[i].xcor()
		yA = myBall.ycor()
		yB = ballsList[i].ycor()
		distance = math.sqrt(math.pow((xB-xA),2) + math.pow((yB-yA),2))
		radiusA = myBall.radius
		radiusB = ballsList[i].radius
		if radiusA + radiusB >= distance:
			if radiusA < radiusB:
				print("You got eaten")
				return(False)
			elif radiusA > radiusB:
				newX = random.randint(-SCREEN_WIDTH + maximumRadius, SCREEN_WIDTH - maximumRadius)
				newY = random.randint(-SCREEN_HEIGHT + maximumRadius, SCREEN_HEIGHT - maximumRadius)
				newSize = random.randint(minimumRadius, maximumRadius)
				ballsList[i].goto(newX, newY)
				ballsList[i].changeSize(newSize)
				ballsList[i].color(random.random(),random.random(),random.random())
				myBall.addToSize(10)

	return(True)
		

#______________________________________________________________________________

for i in range(0,numberOfBalls):
	newBallX = random.randint(-SCREEN_WIDTH + maximumRadius, SCREEN_WIDTH - maximumRadius)
	newBallY = random.randint(-SCREEN_HEIGHT + maximumRadius, SCREEN_HEIGHT - maximumRadius)
	newBallRadius = random.randint(minimumRadius, maximumRadius)
	newBallDx = random.uniform(minimumDx, maximumDx)
	newBallDy = random.uniform(minimumDy, maximumDy)
	while newBallDx == 0 or newBallDy == 0:
		newBallDx = random.uniform(minimumDx, maximumDx)
		newBallDy = random.uniform(minimumDy, maximumDy)
	newBallColor = (random.random(),random.random(),random.random())
	ball = Ball(newBallX, newBallY, newBallRadius, newBallDx, newBallDy, newBallColor)
	ballsList.append(ball)

myBall = Ball(0, -SCREEN_HEIGHT + maximumRadius + 50, 20, -0.3, 0.2, 'red')
myBall.penup()

"""
amountOfFood = 45
foodList = []

for i in range(0,amountOfFood):
	newFoodX = random.randint(-SCREEN_WIDTH + 3, SCREEN_WIDTH - 3)
	newFoodY = random.randint(-SCREEN_HEIGHT + 3, SCREEN_HEIGHT - 3)
	newFoodColor = (random.random(),random.random(),random.random())
	food = Food(newFoodX, newFoodY, newFoodColor)
	foodList.append(food)
"""
def movearound(event):
	myBallX = event.x - SCREEN_WIDTH
	myBallY = SCREEN_HEIGHT - event.y
	myBall.goto(myBallX, myBallY)
	check_myball_collision()

turtle.getcanvas().bind("<Motion>", movearound)


turtle.listen()

while check_myball_collision() == True :
	moveAllBalls(ballsList)	
	turtle.update()