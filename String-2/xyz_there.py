#Return True if the given string contains an appearance of "xyz" where the xyz is
#not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


#xyz_there('abcxyz') → True
#xyz_there('abc.xyz') → False
#xyz_there('xyz.abc') → True

#code
def xyz_there(str):

  while str.count('xyz') !=  0:
    ind = str.index('xyz')
    if ind == 0:
      return True
      break
    elif str[ind-1] != '.':
      return True
      break
    else:
      str = str[:ind]+'ooo'+str[ind+3:]
      
  if str.count('xyz') == 0:
    return False

