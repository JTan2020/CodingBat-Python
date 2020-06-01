#Given a non-empty string like "Code" return a string like "CCoCodCode".


#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'

#code
def string_splosion(str):
  str0 = ''
  for i in range(len(str)):
    str0 = str0 + str[:i+1]
  return str0
