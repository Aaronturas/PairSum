#Finding the sum of two indexes that equal the target(x) using pointers
def isPairSum(lst, x):
  l = len(list)

  ptr1 = 0
  ptr2 = l - 1
  sum = 0

  while(ptr1 < ptr2):
    sum = list[ptr1] + list[ptr2]
    if(list[ptr1] + list[ptr2] != x):
      if(sum > x):
        ptr2-=1
      else:
        ptr1+=1
    elif(list[ptr1] + list[ptr2] == x):
      print("Sum: ", sum)
      return True
  return False

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

x = 30
print(isPairSum(list, x))


