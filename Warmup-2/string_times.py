#Given a string and a non-negative int n, return a larger string that is n copies
#of the original string.


#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'

#code
def string_times(str, n):
  str0 = ''
  for i in range(n):
    str0 = str0 + str
  return str0  
