# Find the sum of all the multiples of 3 or 5 below 1000.
result = 0
for i in range(1000):
    if((i%3==0)or(i%5==0)):
        result += i
print(result)