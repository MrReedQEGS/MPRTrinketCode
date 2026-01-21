#MPR- May 2024
#Compare this to the diagram on page 349 in the OCR textbook and it should make sense!!!
#It is all about move L and R about until R<L then you swap the pivot into its new position.
#It is O(log(n)) and uses less memory than merge sort, so it is the "best"

#I removed the return from the quick sort function, the list is global so never needs returning anywhere!!!

def partition(alist, start, end):
  pivot = alist[start]
  leftmark = start + 1
  rightmark = end
  done = False
  
  while done == False:
    while leftmark <= rightmark and alist[leftmark] <= pivot:
      leftmark = leftmark + 1

    while alist[rightmark] >= pivot and rightmark >= leftmark:
      rightmark = rightmark - 1

    if rightmark < leftmark:
      done = True
    else:
      # swap the list items
      temp = alist[leftmark]
      alist[leftmark] = alist[rightmark]
      alist[rightmark] = temp

  # swap the pivot with alist[rightmark]
  temp = alist[start]
  alist[start] = alist[rightmark]
  alist[rightmark] = temp
  
  return rightmark

def quicksort(alist, start, end):
  print(alist[start:end+1])
  if start < end:
    # partition the list
    split = partition(alist, start, end)
    # sort both halves
    quicksort(alist, start, split-1)
    quicksort(alist, split+1, end)

alist = [9, 5, 4, 15, 3, 8, 11]
quicksort(alist,0,len(alist)-1)
print(alist)
