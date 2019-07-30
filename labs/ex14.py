for i in range(2,10) :
  for j in range(2,i) :
    if i%j == 0 :
      break
  else :
    print(str(i) + " jest liczba pierwsza")
