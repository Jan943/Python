colors = ['red', 'green', 'blue', 'yellow', 'gray']
print(colors[0])
print(len(colors))
print('red' in colors)
print('black' in colors)

list = [0]*100
print(list)

numbers = [1, 2, 3, 4, 5]
print(numbers)

efect = colors + numbers
print(efect)

#efect = ['ziemia'] + efect
efect[0] = 'ziemia'
print(efect)

days_of_week = ['poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela']
#efect[9] = days_of_week #z lista
efect = efect + days_of_week #bez listy
print(efect)

efect.append('merkury')
print(efect)
