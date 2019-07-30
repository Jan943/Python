f = open("plik.txt","r") #liczenie linijek w tekscie

i = 0
for line in f :
  i = i + 1
print("Jest " + str(i) + " linijek")

#for line in f.readlines() : 
 # words = len(line.split(" "))
#print("Linijka " + str(line) + " sklada sie z " + str(words) + " slow")

for line in f :
  vowels = 0
  for letter in line :
    if letter == "A" or letter == "a" or letter == "E" or letter == "e" or letter == "I" or letter == "i" or letter == "O" or letter == "o" or letter == "U" or letter == "u" :
      vowels = vowels + 1
  print("Linijka " + str(line) + " sklada sie z " + str(vowels) + " samoglosek")

for line in f :
  for letter in line :
    if letter == "A" or letter == "a" or letter == "E" or letter == "e" or letter == "I" or letter == "i" or letter == "O" or letter == "o" or letter == "U" or letter == "u" :
      str = letter
      if str.upper() :
print("Linijka " + str(line) + " sklada sie z samogloski napisanej z duzej litery")

