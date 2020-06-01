#Given a string, return a new string made of every other char starting with the
#first, so "Hello" yields "Hlo".


#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'

#code
def string_bits(str):
  str1 = ''
  for i in range(len(str)):
    if i%2 == 0:
      str1 = str1 + str[i]
  return(str1)
