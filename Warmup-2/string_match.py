#Given 2 strings, a and b, return the number of the positions where they contain
#the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx",
#"aa", and "az" substrings appear in the same place in both strings.


#string_match('xxcaazz', 'xxbaaz') → 3
#string_match('abc', 'abc') → 2
#string_match('abc', 'axc') → 0

#code
def string_match(a, b):
  ct = 0
  if len(a) > len(b):
    leng = len(b)
  else:
    leng = len(a)
  for i in range(leng-1):
    if a[i] + a[i+1] == b[i] + b[i+1]:
      ct += 1
  return ct
