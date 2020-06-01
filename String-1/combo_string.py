#Given 2 strings, a and b, return a string of the form short+long+short, with the
#shorter string on the outside and the longer string on the inside. The strings
#will not be the same length, but they may be empty (length 0).


#combo_string('Hello', 'hi') → 'hiHellohi'
#combo_string('hi', 'Hello') → 'hiHellohi'
#combo_string('aaa', 'b') → 'baaab'

#code
def combo_string(a, b):
  str_l = ''
  str_s = ''
  if len(a) >= len(b):
    str_l = a
    str_s = b
  else:
    str_l = b
    str_s = a
  return str_s+str_l+str_s
