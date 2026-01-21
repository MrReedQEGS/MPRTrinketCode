#MPR - May 2024
#This is from page 351 of the text book and it seems to work!!!

GRAPH = { "A":["B","D","E"], "B":["A","C","D"], "C":["B","G"],
"D":["A","B","E","F"], "E":["A","D"] , "F":["D"], "G":["C"]}
#an empty list of visited nodes
visitedList = [] 

def dfs(graph, currentVertex, visited):
  #append currentVertex to list of visited nodes
  visitedList.append(currentVertex)
  for vertex in graph[currentVertex]: # check neighbours
    if vertex not in visited :
      dfs(graph, vertex, visited) # recursive call
      # stack will store return address, parameters and local variable
      #In other words....we do not need to run a separate list of where we are and 
      # where we go when backtracking...recursion does this for us!
  return visited

#main program
traversal = dfs(GRAPH, "A", visitedList)
print("Nodes visited in this order: ", traversal)
