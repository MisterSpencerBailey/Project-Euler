sum1 = 0
sum2 = 0
total = 0
difference = 0

for i in range(101):
    sum1 += i**2
    sum2 += i

sum2 = sum2**2

difference = sum2-sum1

print(difference)
