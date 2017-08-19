def is_prime_number(x): #Checks to find if a number is prime
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True


count = 0
i =0

while count != 10001:
    i += 1
    if is_prime_number(i):
        count +=1
        #print(i)
print(i)
    
