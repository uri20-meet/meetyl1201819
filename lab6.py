import turtle
from turtle import Turtle
turtle.hideturtle()
turtle.colormode(255)
import random

class Rectangle(Turtle):
	def __init__(self, width, height):
		Turtle.__init__(self)
		turtle.width = width
		turtle.height = height
		
		turtle.penup()
		turtle.begin_poly()
		turtle.goto(width, 0)
		turtle.goto(width, height)
		turtle.goto(0, height)
		turtle.goto(0,0)
		turtle.end_poly()
		temp = turtle.get_poly()
		turtle.register_shape("rectangle", temp)
		self.setheading(90)
		self.shape("rectangle")
		

rectangle1 = Rectangle(130,52)
rectangle1.penup()
rectangle1.forward(100)

turtle.hideturtle()
"""
class Square(Rectangle)
	def __init__(self, width, height):
		Rectangle.__init__(self, width, height)
		self.shape("square")
		self.size = size
	def random_color(self):
		r = random.randint(0,256)
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color(r, g, b)

square1 = Square(3)
square1.random_color()
"""


turtle.mainloop()