#Similar to OCR A level paper 1 - word scoring question
#Mark Reed - 15th Jan 2025

word = "oranges"
letters = "yhasrgopner"

score = 0
numInWord = len(word)
numOfAvailableLetters = len(letters)

for i in range(numInWord):
  currentLetter = word[i]
  
  for j in range(numOfAvailableLetters):
    if(letters[j] == currentLetter):
      letters = letters[:j] + "!" + letters[j+1:]
      score = score + 1
      break
  else:
    score = 0

#print(letters)    
print("The word \"" + word + "\" scores " + str(score) + " points!")
      
      
