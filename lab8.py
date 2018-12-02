from turtle import *
import random
import turtle
import math

class Ball(Turtle):
	def __init__(self, x, y, radius, color, speed):
		Turtle.__init__(self)
		self.penup()
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

def check_collision(ballA, ballB):
	xA = ballA.xcor()
	xB = ballB.xcor()
	yA = ballA.ycor()
	yB = ballB.ycor()
	distance = math.sqrt(math.pow((xB-xA),2) + math.pow((yB-yA),2))
	radiusA = ballA.radius
	radiusB = ballB.radius

	if radiusA + radiusB >= distance:
		ballA.color("green")
		ballB.color("black")
		if radiusA < radiusB:
			newX = random.randint(-150, 150)
			newY = random.randint(-150, 150)
			ballA.goto(newX, newY)
		elif radiusA > radiusB:
			newX = random.randint(-150, 150)
			newY = random.randint(-150, 150)
			ballB.goto(newX, newY)

def collisionInList(listOfBalls):
	for i in range(0,len(listOfBalls)):
		for q in range(i+1,len(listOfBalls)):
			check_collision(listOfBalls[i], listOfBalls[q])

ball1 = Ball(-50 , 50, 40, "blue", 1)

ball2 = Ball(55, 50, 65, "red", 1)

ball3 = Ball(0, -95, 50, "yellow", 1)

ballsList = [ball1, ball2, ball3]

#check_collision(ball1, ball2)
collisionInList(ballsList)

turtle.mainloop()