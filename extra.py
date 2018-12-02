import turtle
from turtle import Turtle
import math
#turtle.tracer(0)

width = 350
height = 150

class Ball(Turtle):
	def __init__(self, x, y, radius, dx, dy, speed, color):
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
		self.speed(speed)

	def move(self):
		global width, height

		oldX = self.xcor()
		oldY = self.ycor()
		newX = oldX + self.dx
		newY = oldY + self.dy
		absX = math.fabs(newX)
		absY = math.fabs(newY)

		if absX >= width:
			self.dx = -self.dx
		if absY >= height:
			self.dy = -self.dy

		print(newX, newY)
		self.goto(newX, newY)



bob = Ball(100, 0, 30, 2, 3, 5, "green")
john = Ball(0, 0, 20, 3, 2, 8, "blue")
kevin = Ball(-100, 0, 30, 2, 2, 6, "red")

while True:
	bob.move()

turtle.mainloop()



#turtle.getscreen().update()