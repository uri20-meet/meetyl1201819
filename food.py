import turtle
from turtle import Turtle

class Food(Turtle):
	def __init__(self, x, y, color):
		Turtle.__init__(self)
		self.penup()
		self.goto(x, y)
		self.shape("circle")
		self.color(color)
		self.shapesize(0.4)