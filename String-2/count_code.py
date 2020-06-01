#Return the number of times that the string "code" appears anywhere in the given
#string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


#count_code('aaacodebbb') → 1
#count_code('codexxcode') → 2
#count_code('cozexxcope') → 2

#code
def count_code(str):
  ct = 0
  while str.count('co') != 0:
    ind = str.index('co')
    if ind + 3 <= len(str) - 1:
      if str[ind+3] =='e':
        ct += 1
        str = str[:ind]+'xxxx'+str[ind+4:]
      else:
        str = str[:ind]+'xx'+str[ind+2:]  
    else:
      str = str[:ind]+'xx'+str[ind+2:]
  return ct
