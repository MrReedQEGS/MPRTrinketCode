#################################################
# HOW TO DISPLAY THINGS FROM A LIST IN A TABLE
#
# Written by Mr Reed
#################################################

players = ["GAMER TAG","fred","bob","jim"]
XP =      ["XP",52,23,0]

#Work out how wide the table needs to be
colWidth = 15
numOfColumns = 2
HorizontalWidth = numOfColumns*colWidth + (numOfColumns+1)

#Print the titles
print("-"*HorizontalWidth) #Draw horizontal bar
print("|{:^{a}}|{:^{a}}|".format(players[0],XP[0],a=colWidth))
print("-"*HorizontalWidth) #Draw horizontal bar

#Print the players
for i in range(1,len(players)):
  someGamerTag = players[i]
  someXP = XP[i]
  print("|{:^{a}}|{:^{a}}|".format(someGamerTag,someXP,a=colWidth))

#Print the final horizontal bar
print("-"*HorizontalWidth) #Draw horizontal bar
