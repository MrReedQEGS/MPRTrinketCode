#MPR - Nov 2023
#8 out of 8 scored!

def CheckRows():
  row1Total=int(finalList1[0])+int(finalList1[1])+int(finalList1[2])
  row2Total=int(finalList2[0])+int(finalList2[1])+int(finalList2[2])
  row3Total=int(finalList3[0])+int(finalList3[1])+int(finalList3[2])
  
  if(row1Total == row2Total == row3Total):
    return row1Total
  else:
    return "muggle"
    
def CheckCols():
  col1Total = int(finalList1[0])+int(finalList2[0])+int(finalList3[0])
  col2Total = int(finalList1[1])+int(finalList2[1])+int(finalList3[1])
  col3Total = int(finalList1[2])+int(finalList2[2])+int(finalList3[2])
  
  if(col1Total == col2Total == col3Total and col1Total):
    return col1Total
  else:
    return "muggle"

def CheckDiags():
  diag1Total = int(finalList1[0])+int(finalList2[1])+int(finalList3[2])
  diag2Total = int(finalList1[2])+int(finalList2[1])+int(finalList3[0])
  
  if(diag1Total == diag2Total):
      return diag1Total
  else:
      return "muggle"


#########################
# MAIN BODY

#sort input strings so they are lists
line1 = input()
line2 = input()
line3 = input()
finalList1 = line1.split(" ")
finalList2 = line2.split(" ")
finalList3 = line3.split(" ")

#Check for muggleness
rowTotal = CheckRows()
colTotal = CheckCols()
diagTotal = CheckDiags()
    
#print("{} {} {}".format(rowTotal,colTotal,diagTotal))
    
#results
if(rowTotal == colTotal == diagTotal and diagTotal != "muggle"):
  print("magic")
else:
  print("muggle")
