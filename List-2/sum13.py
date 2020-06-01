#Return the sum of the numbers in the array, returning 0 for an empty array.
#Except the number 13 is very unlucky, so it does not count and numbers that
#come immediately after a 13 also do not count.


#sum13([1, 2, 2, 1]) → 6
#sum13([1, 1]) → 2
#sum13([1, 2, 2, 1, 13]) → 6


#code
def sum13(nums):
  while nums.count(13) != 0:
    ind13 = nums.index(13)
    nums[ind13] = 0
    if nums[ind13] != nums[-1] and nums[ind13+1] != 13:
      nums[ind13+1] = 0
    else:
      continue
  return sum(nums)
