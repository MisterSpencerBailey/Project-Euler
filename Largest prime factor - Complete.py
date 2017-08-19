def is_prime_number(x): #Checks to find if a number is prime
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

i = 0
greatest = 0
index = 600851475143/2
index = int(index+1)


for i in range (index):
    if i % 2 != 0:
        if is_prime_number(i):
            greatest = i
    i += 1

print(greatest)
