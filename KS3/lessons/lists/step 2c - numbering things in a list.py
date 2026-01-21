#################################################
# HOW TO NUMBER EVERYTHING IN A LIST
#
# Written by Mr Reed
#################################################

carsList = ["BMW","Ford","Fiat","Peugeot"]

print("Some cars")
print("*********")
for i in range(0,4):
  print(str(i) + " : " + carsList[i])

print()
print()
print("A better way?")
print()
  
#Also...Look how we can easily start the numbers at 1 instead

print("Some cars")
print("*********")
for i in range(0,4):
  print(str(i+1) + " : " + carsList[i])
