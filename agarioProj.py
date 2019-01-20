import turtle
from turtle import Turtle
import food
from food import Food
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
		collisionInTwoGroups(ballsList, foodList)
		collisionInTwoGroups(listOfMyBall, foodList)

	def addToSpeed(self, addition):
		
		if self.dx > 0:
			self.dx += addition
		else:
			self.dx -= addition
		if self.dy > 0:
			self.dy += addition
		else:
			self.dy -= addition

	def addToSize(self, addition):
		
		self.radius += addition
		self.shapesize(self.radius/10)

	def changeSize(self, newSize):
		
		self.radius = newSize
		self.shapesize(self.radius/10)

	def getRadius(self):
		theRadius = self.radius
		return(theRadius) 

#_______________________________________________________________________________

def moveAllBalls(allBalls):
	for i in allBalls:
		i.move()
#_______________________________________________________________________________

numberOfBalls = 9
minimumRadius = 10
maximumRadius = 40
minimumDx = -3
maximumDx = 3
minimumDy = -3
maximumDy = 3
ballsList = []


def check_collision(ballA, ballB):
	global SCREEN_WIDTH, SCREEN_HEIGHT
	xA = ballA.xcor()
	xB = ballB.xcor()
	yA = ballA.ycor()
	yB = ballB.ycor()
	distance = math.sqrt(math.pow((xB-xA),2) + math.pow((yB-yA),2))
	radiusA = ballA.radius
	radiusB = ballB.radius
	if radiusA + radiusB >= distance:

		if radiusA < radiusB:
			newX = random.randint(int(-SCREEN_WIDTH + maximumRadius), int(SCREEN_WIDTH - maximumRadius))
			newY = random.randint(int(-SCREEN_HEIGHT + maximumRadius), int(SCREEN_HEIGHT - maximumRadius))
			newSize = random.randint(minimumRadius, maximumRadius)
			ballA.goto(newX, newY)
			ballA.changeSize(newSize)
			ballA.color(random.random(),random.random(),random.random())
			ballB.addToSize(10)

		elif radiusA > radiusB:
			newX = random.randint(int(-SCREEN_WIDTH + maximumRadius), int(SCREEN_WIDTH - maximumRadius))
			newY = random.randint(int(-SCREEN_HEIGHT + maximumRadius), int(SCREEN_HEIGHT - maximumRadius))
			newSize = random.randint(minimumRadius, maximumRadius)
			ballB.goto(newX, newY)
			ballB.changeSize(newSize)
			ballB.color(random.random(),random.random(),random.random())
			ballA.addToSize(10)

		return(True)
	else:
		return(False)

def check_eaten(ball, food):
	global SCREEN_HEIGHT, SCREEN_WIDTH
	xB = ball.xcor()
	xF = food.xcor()
	yB = ball.ycor()
	yF = food.ycor()
	distance = math.sqrt(math.pow((xF-xB),2) + math.pow((yF-yB),2))
	radiusB = ball.radius
	radiusF = 2
	if radiusB + radiusF >= distance:
		newX = random.randint(int(int(-SCREEN_WIDTH + maximumRadius)), int(SCREEN_WIDTH - maximumRadius))
		newY = random.randint(int(int(-SCREEN_HEIGHT + maximumRadius)), int(SCREEN_HEIGHT - maximumRadius))
		food.penup()
		food.goto(newX, newY)
		food.color(random.random(),random.random(),random.random())
		ball.addToSize(2)
		
		return(True)
	else:
		return(False)


def collisionInList(listOfBalls):
	collided = False
	for i in range(0,len(listOfBalls)):
		for q in range(i+1,len(listOfBalls)):
			if check_collision(listOfBalls[i], listOfBalls[q]) and listOfBalls[i] !=listOfBalls[q] :
				collided = True

def collisionInTwoGroups(list1, list2):
	collided = False
	for i in range(0,len(list1)):
		for q in range(0,len(list2)):
			if check_eaten(list1[i], list2[q]):
				collided = True

def check_myball_collision():
	global SCREEN_HEIGHT, SCREEN_WIDTH
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
				newX = random.randint(int(-SCREEN_WIDTH + maximumRadius), int(SCREEN_WIDTH - maximumRadius))
				newY = random.randint(int(-SCREEN_HEIGHT + maximumRadius), int(SCREEN_HEIGHT - maximumRadius))
				newSize = random.randint(minimumRadius, maximumRadius)
				ballsList[i].goto(newX, newY)
				ballsList[i].changeSize(newSize)
				ballsList[i].color(random.random(),random.random(),random.random())
				myBall.addToSize(10)

	return(True)
		

#______________________________________________________________________________
def CreateBalls(number):
	global SCREEN_HEIGHT, SCREEN_WIDTH, minimumDx, maximumDx, minimumDy, maximumDy, maximumRadius, minimumRadius 
	for i in range(0,numberOfBalls):
		newBallX = random.randint(int(-SCREEN_WIDTH + maximumRadius), int(SCREEN_WIDTH - maximumRadius))
		newBallY = random.randint(int(-SCREEN_HEIGHT + maximumRadius), int(SCREEN_HEIGHT - maximumRadius))
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
listOfMyBall = [myBall]

foodList = []

def CreateFood(amount):
	global SCREEN_WIDTH, SCREEN_HEIGHT
	for i in range(0,amount):
		newFoodX = random.randint(int(-SCREEN_WIDTH + 3), int(SCREEN_WIDTH - 3))
		newFoodY = random.randint(int(-SCREEN_HEIGHT + 3), int(SCREEN_HEIGHT - 3))
		newFoodColor = (random.random(),random.random(),random.random())
		food = Food(newFoodX, newFoodY, newFoodColor)
		foodList.append(food)

CreateBalls(numberOfBalls)
CreateFood(20)

def SpeedAllBy(addition):
	for i in ballsList:
		i.addToSpeed(addition)



def movearound(event):
	global SCREEN_WIDTH, SCREEN_HEIGHT
	myBallX = event.x - SCREEN_WIDTH
	myBallY = SCREEN_HEIGHT - event.y
	myBall.goto(myBallX, myBallY)
	check_myball_collision()

turtle.getcanvas().bind("<Motion>", movearound)


turtle.listen()

while check_myball_collision() == True :
	if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
		CreateBalls(5)
		CreateFood(35)
		SpeedAllBy(4.5)
	moveAllBalls(ballsList)	
	if myBall.getRadius() >= turtle.getcanvas().winfo_height()/2:
		print("YOU WON THE GAME")
	turtle.update()
