#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears
#in the array somewhere.


#array123([1, 1, 2, 3, 1]) → True
#array123([1, 1, 2, 4, 1]) → False
#array123([1, 1, 2, 1, 2, 3]) → True

#code
def array123(nums):
  #print(str(nums))
  if str(nums).count('1, 2, 3')!=0:
    return True
  else:
    return False
