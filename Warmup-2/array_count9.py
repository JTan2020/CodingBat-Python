#Given an array of ints, return the number of 9's in the array.


#array_count9([1, 2, 9]) → 1
#array_count9([1, 9, 9]) → 2
#array_count9([1, 9, 9, 3, 9]) → 3

#code
def array_count9(nums):
  str0 = str(nums).strip()
  ct = str0.count('9')
  return ct
