#Given 3 int values, a b c, return their sum. However, if one of the values is
#13 then it does not count towards the sum and values to its right do not count.
#So for example, if b is 13, then both b and c do not count.


#lucky_sum(1, 2, 3) → 6
#lucky_sum(1, 2, 13) → 3
#lucky_sum(1, 13, 3) → 1

#code
def lucky_sum(a, b, c):
  lis = [a,b,c]
  while 13 in lis:
    ind = lis.index(13)
    for i in range(len(lis)-ind):
      lis[i+ind] = 0
  return sum(lis)
