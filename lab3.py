import turtle
turtle.addshape("face.gif")
turtle.shape("face.gif")
turtle.speed(10000)
dist1 = 200
dist2 = 75
dist3 = 30
angle = 45

for i in range(360):
	turtle.right(i)
	turtle.pendown()
	turtle.forward(dist1)
	turtle.right(angle)
	turtle.forward(dist2)
	turtle.right(2 * angle)
	turtle.forward(dist3)
	turtle.penup()
	turtle.home()


turtle.mainloop()