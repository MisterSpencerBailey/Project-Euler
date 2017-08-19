finex = 2**1000 #Final Exponent
string_finex = str(finex)
length = len(string_finex)
i = 0
total = 0

while i != length:	
    total += int(string_finex[i])
    i+=1

print(total)
