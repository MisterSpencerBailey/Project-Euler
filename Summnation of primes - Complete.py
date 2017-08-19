prime_numbers = 0
total = 0

def is_prime_number(x): #Checks to find if a number is prime
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True
	        

for i in range(int(input("How many numbers you wish to check: "))):
    if is_prime_number(i):
        prime_numbers += 1
        print (i)
        total += i
    
print(total)
