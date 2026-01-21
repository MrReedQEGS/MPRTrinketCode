import time,random

def PrintDelay(someWord):
  for letter in someWord:
    print(letter,end="",flush=True)
    time.sleep(random.uniform(0.05,0.25))
  print()

def InputDelay(someWord):
  for letter in someWord:
    print(letter,end="",flush=True)
    time.sleep(random.uniform(0.05,0.25))
    
  ans = input()
  return ans
  
PrintDelay("""
Hello.
  I am a human!!!
  """)
name = InputDelay("What is your name? ")
PrintDelay(name + " is a cool name!")
