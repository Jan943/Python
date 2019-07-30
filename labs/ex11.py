day = int(input("Please write number of the date: "))
month = int(input("Please write number of the month: "))

if month <= 3 :
  if month < 3 or day < 21 :
    print("Winter")
  else :
    print("Spring")
elif month <= 6 :
  if month < 6 or day < 22 :
    print("Spring")
  else :
    print("Summer")
elif month <= 9 :
  if month < 9 or day < 23 :
    print("Summer")
  else :
    print("Autumn")
elif month <=12 :
  if month < 12 or day < 22 :
    print("Autumn")
  else :
    print("Winter")
else :
  print("Wrong data")
