#odwolywanie sie do elementu spoza zakresu

x = [0, 1, 2, 3]
try :
  x[4] = 0
except IndexError :
  print("Index error")

#blad w kluczu

x = {
"wreszcie": 1,
"zobacze": 2,
"Marylin": 3
}

try :
  print(x["nie_zobacze"])
except KeyError:
  print("Key error")
