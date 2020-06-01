#Return the sum of the numbers in the array, except ignore sections of numbers
#starting with a 6 and extending to the next 7 (every 6 will be followed by at
#least one 7). Return 0 for no numbers.


#sum67([1, 2, 2]) → 5
#sum67([1, 2, 2, 6, 99, 99, 7]) → 5
#sum67([1, 1, 6, 7, 2]) → 4


#code
def sum67(nums):
  add = 0
  while nums.count(6) and nums.count(7):
    ind6 = nums.index(6)
    ind7 = nums.index(7)
    if ind7 > ind6:
      nums = nums[:ind6] + nums[ind7+1:]
    else:
      nums = nums[:ind7]+nums[ind7+1:]
      add += 7
  return sum(nums) + add
