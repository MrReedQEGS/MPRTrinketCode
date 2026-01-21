#Mr Reed - 2024
#All of the following code could help you make random elements for you 
#ANPR letters to customers that must have a fine!
import random

#Here is some code that makes a random number
print("A random number...")
num = random.randint(100,200)
print(num)
print()

#Here is some code that makes a random letter of the alphabet
print("A random letter of the alphabet...")
letter = random.randint(65,65+26)
print(chr(letter))
print()

#Here is one more piece of code that makes that START of a random phone number
print("The start of a random phone number...")
random3Digits = ""
for i in range(3):
  random3Digits = random3Digits + str(random.randint(0,9))

print("PHONE NUM : " + "07" + random3Digits)
