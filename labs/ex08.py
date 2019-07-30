dict = {"Polska":"Warszawa", "Niemcy":"Berlin", "Slowacja":"Bratyslawa", "Czechy":"Praga"}
#dict = dict + {"Francja":"Paryz"}
#dict = ["Francja"] = "Paryz"
print(dict)
#dict.update({"jeden" : 1}) #udalo sie - inna funkcja!
dict ["jeden"] = 1
print(dict)
#dict.update({"Polska":"Krakow"}) #zamiana wartosci - inna funkcja!
dict ["Polska"] = "Kraków" #blad encoding
print(dict)
dict.update({"Polska":"Gniezno"})
print(dict) #zamiana
