#Saving up - OUCC 2023
#MPR - Nov 2023
#This one seems really easy!?!?!?
#It scores 6 out of 6  :)

#Test data
#
#Answer - 10

#Task:
#Write a program that totals Kaleisha's daily earnings and outputs how many days it would have taken her, in the provided 20 days, to save £1000. Your program must also remove the student's £20 daily expenses.


#All integers in the input will be less than or equal to 200.
#The data provided will always be enough to save £1000 by the 20th day.
#Input format:
#A single row of 20 integers separated by spaces.
#Output format:
#An integer.

DAILY_EX = 20
TARGET = 1000
totalSoFar = 0
days = 0

data = input()
dataList = data.split(" ")
finalList = []
for thing in dataList:
  finalList.append(int(thing))

while(totalSoFar < TARGET):
  totalSoFar = totalSoFar + finalList[days] - DAILY_EX
  days = days + 1

print(days)
  

