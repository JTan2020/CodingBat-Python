#Given an array of ints, return True if the array contains a 2 next to a 2
#somewhere.


#has22([1, 2, 2]) → True
#has22([1, 2, 1, 2]) → False
#has22([2, 1, 2]) → False


#code
def has22(nums):
  str1 = str(nums)
  return '2, 2' in str1
