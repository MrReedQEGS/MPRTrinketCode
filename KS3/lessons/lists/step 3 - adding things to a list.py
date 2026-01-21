#################################################
# HOW TO ADD ONE THING TO THE END OF A LIST
#
# Written by Mr Reed
#################################################

#Make a list
animals = ["bat","ant","frog","cow"]

#print the list
print("BEFORE")
print(animals)
print()          #Blank line

#Ask the user for a new animal
newAnimal = input("Animal to add to the list: ")
print()          #Blank line

#Add it to the END of the list
animals.append(newAnimal)

#print the list again...to show that it worked!
print("AFTER")
print(animals)














