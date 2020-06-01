#Given an int array length 2, return True if it contains a 2 or a 3.


#has23([2, 5]) → True
#has23([4, 3]) → True
#has23([4, 5]) → False


#code
def has23(nums):
  if nums.count(2) or nums.count(3):
    return True
  else:
    return False
