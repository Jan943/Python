list = [0]*50
print(list[49])
list[0] = 1
list[1] = 2
print(list)
for i in range(0,47) :
  list[i+2] = (list[i+1] + list[i])/(list[i+1] - list[i])
print(list)
sum = 0
for j in range(0,49) :
  sum = sum + list[j]
print(sum) 
medium =(list[24] + list[25])/2
print(medium)
