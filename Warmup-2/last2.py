#Given a string, return the count of the number of times that a substring length
#2 appears in the string and also as the last 2 chars of the string, so "hixxxhi"
#yields 1 (we won't count the end substring).


#last2('hixxhi') → 1
#last2('xaxxaxaxx') → 1
#last2('axxxaaxx') → 2

#code
def last2(str):
  ct = 0
  str0 = ''
  if len(str) >= 2:
    str0 = str[len(str)-2] + str[len(str)-1]
    for i in range(len(str)-2):
      if str[i] + str[i+1] == str0:
        ct += 1
  return ct
