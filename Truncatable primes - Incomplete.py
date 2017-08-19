trunctable = 0
total = 0
primes = [2,3,5,7,13,17,19]
i = 20


def is_prime_number(x): #Checks to find if a number is prime
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True


while trunctable != 11:
    i += 1
    i_string = str(i)
    if is_prime_number(i):
        primes.append(i)
        if i_string[::-1] not in primes:
            break
        else:
            if i in primes:
                total += i
                trunctable += i
    
                
print(total)
                
    
