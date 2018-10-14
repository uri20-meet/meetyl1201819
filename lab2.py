#EXERCISE 1
def makeNewList(list):
	first = list[0]
	last = list[-1]
	newList=[first,last]
	print(newList)
#makeNewList([1,2,3,4,5,6,])


#EXERCISE 2
a = [1,1,2,3,5,8,13,21,34,55,89]

def printBelowFive(x):
	listBelowFive=[]
	for value in x:
		if value < 5:
			listBelowFive.append(value)
	print(listBelowFive)
#printBelowFive(a)


#EXERCISE 3
a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
finalList=[]
def compare(list1, list2):
	global finalList
	for value1 in list1:
		for value2 in list2:
			if value1==value2:
				if not value1 in finalList:
					finalList.append(value1)
compare(a,b)
#print(finalList)


#EXERCISE 4

userNum=int(input("Type A Number!"))
prime=False
for i in range(userNum):
	if i != 0 and i != 1:
		leftover = userNum%i
		if leftover==0:
			prime=True

#if prime == True:
#	print("The Number Is Prime!")
#else:
#	print("Not Prime")
