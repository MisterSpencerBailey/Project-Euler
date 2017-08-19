current = 0
current_string =""
greatest = 0
a = 100
b = 100

while a < 1000:
    current = a*b
    current_string = str(current)
    
    if current_string[::-1] == current_string:
        if current > greatest:
            greatest = current


    b +=1
    
    if b > 999:
        b = 100
        a += 1
        


print(greatest)
