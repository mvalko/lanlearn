#test
from os import listdir
import random

lanlist = listdir('lan')

def menu():
    print("Main Menu")

def match():
    score = 0
    #while usrinput not '0':
    random = random.choice(list(lan.article.key()))# pull random dict entry
    usrinput = (input("type in definition")).lower
        #if usrinput is lan.article[random]:
        #    score += 1
        #    print("Correct! Current Score is: " + score)
        #else:
           # score -= 1
           # print("Correct answer was: " + lan.article[random])
           # print("Current score is: " + score)
# imports the specific language module
def lanselect(lan):
	import lan
	print("Succesfully loaded the " + lan + " Language!")
	mainMenu()

# lists available lan modules
def availan():
	print("Available Languages: ")
	for i in range(len(lanlist)): # prints out a legible index value and available Languages
		print(i, end = " ")
		print(lanlist[i])
	lanselect(lanlist[int(input("Enter index value of the desired language: "))].strip('.py')

menu():