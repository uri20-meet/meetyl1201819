# PROBLEM 1


"""
import tkinter as tk
from tkinter import simpledialog
#Then when ever you want to ask the user for input use this code
greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
if greeting in ["Arrr!"]:
    print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!")
"""


# PROBLEM 2


"""
# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

import tkinter as tk
from tkinter import simpledialog

year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))

if year <= 1900:
    print("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print("That's totally the present!")
else:
    print ("Far out, that's the future!!")
"""


# PROBLEM 3


"""
# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".

class Person(object):
	def __init__(self, first_name, last_name):
		self.first = first_name
		self.last = last_name
	def speak(self):
		print("My name is " + self.last + ", " + self.first)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.speak()
"""


#PROBEM 4


"""
import tkinter as tk
from tkinter import simpledialog
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average    Grade
# 90+        A
# 80-89      B
# 70-79      C
# 60-69      D
# 0-59       F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam1 = int(simpledialog.askstring("Input", "Input exam grade one: ", parent=tk.Tk().withdraw()))

exam2 = int(simpledialog.askstring("Input", "Input exam grade two: ", parent=tk.Tk().withdraw()))

exam3 = int(simpledialog.askstring("Input", "Input exam grade three: ", parent=tk.Tk().withdraw()))

grades = [exam1, exam2, exam3]
sum = 0
for grade in grades:
	sum = sum + grade

avg = int(sum / len(grades))

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 60 and avg < 70:
    letter_grade = "D"
else:
    letter_grade = "F"


print("Exams: " + str(exam1) + ", " + str(exam2) + ", " + str(exam3))

print("Average: " + str(avg))

print("Grade: " + str(letter_grade))

if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")
"""



#PROBLEM 5


"""
class Person(object):
   def __init__(self, name, favorite_food, age):
       self.name = name
       self.fav_food = favorite_food
       self.age = age


   def define_color(self, color):
       self.color = color

   def print_info(self):
       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.fav_food + " and my favorite color is " + self.color)


a = Person("Britney", "Pizza", 16)
a.define_color("Black")
a.print_info()

b = Person("Jake", "Chocolate", 15)
b.define_color("Red")
b.print_info()
"""



#PROBLEM 6


"""
class Bear(object):
	def __init__(self, name):
		self.name = name
		print("A new bear created. Its name is: " + self.name)
    
	def say_hi(self):
		print("Hi! I’m a bear. My name is " + self.name)

my_bear = Bear("Danny")
my_bear.say_hi()
"""



#PROBLEM 7


"""
balloons = 5
name = "Ron"
color = "Yellow"
print("This is a tale about " + str(balloons) + " balloons. The first kid is " + name + " who got a " + color + " balloon")
"""



#PROBLEM 8


"""
class Cake(object):
    def __init__(self, flavor):
        self.cake_flavor = flavor

    def eat(self):
        print("Yummy!!! Eating a ", self.cake_flavor, "cake :)")

cake = Cake("chocolate")
cake.eat()
# what I want to be printed: Yummy!!! Eating a chocolate cake :)
"""


#PROBLEM 9



class Cat(object):
	def __init__(self, name):
		self.name = name
		self.age = 0
	def birthday(self, finalAge):
		for i in range(self.age, finalAge):
			
			self.age += 1
			
			if i%10 == 0:
				finish = "st"
			elif i%10 == 1:
				finish = "nd"
			elif i%10 == 2:
				finish = "rd"
			else:
				finish = "th"

			if self.age >= 100:
				print("Dong dong, the cat is dead!")
			else:
				print(self.name + " has its " + str(self.age) + finish +' birthday!')
my_cat = Cat("Salem")
my_cat.age+=1
my_cat.birthday(8)

# what I want: my cat to celebrate its 8th birthday (and all the 
# birthdays that come before that)
