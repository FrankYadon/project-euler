# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
primes = [2, 3, 5, 7, 11, 13, 17, 19]
answer = 1
for num in primes:
    i = 1
    while (num ** (i+1)) < 20:
        i += 1
    answer = answer * (num ** i)
print(answer)
