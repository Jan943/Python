day = int(input("Please write number of the date: "))
month = int(input("Please write number of the month: "))

if month in (12,1,2,3) and ((month == 3 and day < 21) or (month == 12 and day > 21)) :
  print("Winter")
elif month in (3,4,5,6) and ((month == 6 and day < 22) or (month == 3 and day > 20)) :
  print("Spring")
elif month in (6,7,8,9) and ((month == 9 and day < 23) or (month == 6 and day > 21)) :
  print("Summer")
elif month in (9,10,11,12) and ((month == 12 and day < 22) or (month == 9 and day > 22)):
  print("Autumn")
else :
  print("Wrong data")


