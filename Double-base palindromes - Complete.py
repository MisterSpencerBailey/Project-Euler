total = 0
i = 0
def dec_to_bin(x):
    return int(bin(x)[2:])


while i != 1000000:
    i_string = str(i)
    i_decimal = str(dec_to_bin(i))
    if i_string == i_string[::-1] and i_decimal == i_decimal[::-1]:
        total += i
        print 
    i += 1

print(total)
