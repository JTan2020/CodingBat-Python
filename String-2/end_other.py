#Given two strings, return True if either of the strings appears at the very end
#of the other string, ignoring upper/lower case differences (in other words, the
#computation should not be "case sensitive"). Note: s.lower() returns the
#lowercase version of a string.


#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True
#end_other('abc', 'abXabc') → True

#code
def end_other(a, b):
  longs = ''
  shorts = ''
  if len(a)>=len(b):
    longs = a.lower()
    shorts = b.lower()
  else:
    longs = b.lower()
    shorts = a.lower()
  if longs[len(longs)-len(shorts):] == shorts:
    return True
  else:
    return False
