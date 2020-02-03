from os import listdir
import random

# makes an array of all the language modules in the lan dir
langlist = listdir('lan')
score = 0

# main game operating function
def match():
    # pulls random article dict entry
    random = random.choice(list(lan.article.key()))
    usrinput = (input("Type in definition: ")).lower

# imports the specific lang module
def langselect():
    import lan
    print("SUccesfully loaded the " + lan + " Language!")


# lists availalbe langs
def availang():
    print("Available Languages: ")
    # prints out a legible index value and availalbe langs
    for i in range(len(langlist)):
        print(i, end = " ")
        print(langlist[i])
    langselect(langlist[int(input("Enter index value of the desired language: "))].strip('.py'))

availang()