#We have a loud talking parrot. The "hour" parameter is the current hour time in
#the range 0..23. We are in trouble if the parrot is talking and the hour is
#before 7 or after 20. Return True if we are in trouble.


#parrot_trouble(True, 6) → True
#parrot_trouble(True, 7) → False
#parrot_trouble(False, 6) → False


#code
def diff21(n):
  if n<21:
    return abs(21-n)
  else:
    return abs(21-n)*2
