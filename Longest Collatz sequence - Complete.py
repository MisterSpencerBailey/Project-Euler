total = 0
count = 0
greatest = 0
i = 1000000


while i != 1:

    while total > 1:

        if total % 2 == 0:
            total = total/2
            count += 1
            #print(total)
        elif total % 2 != 0:
            total = (3*total)+1
            count += 1
            #print(total)


    if count > greatest:
        greatest = count
        print(greatest, i)
        
    i -= 1
    total = i
    count = 0

print(greatest)
    
        
        
