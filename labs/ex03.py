x =int(input("Prosze podaj liczbe: "))
#wlasne
if x == 0 or x == 1 :
 print("Silnia wynosi 1")
else :
 z = 1
 while x > 1 :
  z = z * x
  x = x - 1
 print(z)
#iter
def silnia_iter(x) :
  z = 1
  if x in (0,1) :
    return 1
  else :
    for i in range(2,x+1) :
      z = z*i
    return z
print silnia_iter(6)
#rek
def silnia_rek(x) :
  if x>1 :
    return x*silnia_rek(x-1)
  elif x in (0,1) :
    return 1
print silnia_rek(5)
