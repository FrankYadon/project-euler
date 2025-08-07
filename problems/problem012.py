# Project Euler Problem 12
# https://projecteuler.info/problem=12
# What is the value of the first triangle number to have over five hundred divisors?

# Find an adequate number of primes
primes = []
end = 20000
test = list(range(end))
for n in range(2, end):
    if test[n] != 0:
        primes.append(n)
        for num in range(n*n, end, n):
            test[num] = 0

# Generate triangle numbers up to 500 factors
factor = 1
a = 2
while factor < 500:
    tri = a * (a + 1) // 2
    temp_tri = tri
    factor = 1
    # Check number of factors
    for pri in primes:
        exponent = 0
        while temp_tri % pri == 0:
            temp_tri //= pri
            exponent += 1
        factor *= exponent + 1
        if factor >= 500:
            print(tri)
            break
    a += 1
