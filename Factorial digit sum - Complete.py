import math

factoral = math.factorial(100)
total = 0
length = len(str(factoral))
factoral = str(factoral)

for i in range(len(str(factoral))):
    total += int(factoral[i])

print(total)
