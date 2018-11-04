
#PROBEM 1 + 2
class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yummy!! " + self.name + " is eating " + food)
	def description(self):
		print(self.name + " is " + str(self.age) + " years old and loves the color " + self.favorite_color)
	def make_sound(self, repNum):
		print(repNum * self.sound)


x = Animal("Woof! ","Bobby",6,"White")
x.eat("Hotdog")
x.description()
x.make_sound(12)



#PROBLEM 3
class Person(object):
	def __init__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat(self,fav_breakfast):
		print(self.name + " is eating " + fav_breakfast)
	def do_sport(self, sport):
		print(self.name + " is " + sport)

y = Person("McBelvin",31,"Jerusalem","Male")
y.eat("pancakes")
y.do_sport("running")


#EXTRA
class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for i in range(len(self.lyrics)):
			print(self.lyrics[i])

flowerSong = Song(["Roses are red," , "Violets are blue" , "I wrote this poem for you."])
flowerSong.sing_me_a_song()
