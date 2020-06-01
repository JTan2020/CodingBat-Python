#Given a string, return a string where for every char in the original, there are
#two chars.


#double_char('The') → 'TThhee'
#double_char('AAbb') → 'AAAAbbbb'
#double_char('Hi-There') → 'HHii--TThheerree'

#code
def double_char(str):
  str1 = ''
  for x in str:
    str1 += x + x
  return str1
