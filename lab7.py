from turtle import *
import random
import turtle
import math

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
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

def collisionInList(listOfBalls):
	for i in range(0,len(listOfBalls)):
		for q in range(i+1,len(listOfBalls)):
			check_collision(listOfBalls[i], listOfBalls[q])

ball1 = Ball(40, "blue", 1)
ball1.penup()
ball1.goto(-50,50)

ball2 = Ball(65, "red", 1)
ball2.penup()
ball2.goto(55,50)

ball3 = Ball(50, "yellow", 1)
ball3.penup()
ball3.goto(0,-95)

ballsList = [ball1, ball2, ball3]

#check_collision(ball1, ball2)
collisionInList(ballsList)

turtle.mainloop()