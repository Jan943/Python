try :
  temp = float(input("Podaj temperature: "))
except ValueError :
  print("Nieprawidlowa temperatura")
scale = input("Podaj skale(F lub C): ")
if scale == "F" :
  T = ((temp) - 32)*5/9
  print("Temperatura w stopniach Celsjusza to: "+ str(T) + " C")
elif scale == "C" :
  F = (temp)*9/5 + 32
  print("Temperatura w Fahrenheitach to: " + str(F) + " F")
else :
  print("Nieprawidlowa skala")
