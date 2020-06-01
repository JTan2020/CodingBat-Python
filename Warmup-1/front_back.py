#Given a string, return a new string where the first and last chars have been
#exchanged.


#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

#code
def front_back(str):
  if len(str)>=3:
    fchar = str[0]
    bchar = str[len(str)-1]
    mstr = str[1:len(str)-1]
    return(bchar+mstr+fchar)
  elif len(str)==2:
    fchar = str[0]
    bchar = str[1]
    return(bchar+fchar)
  else:
    return(str)
