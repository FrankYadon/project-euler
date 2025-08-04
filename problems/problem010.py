# Find the sum of all the primes below two million.
primes = 0
start = 2
end = 2000000
numbers = [True] * end
for n in range(2 , end):
    if numbers[n]:
        primes += n
        for comp in range(n*n, end, n):
            numbers[comp] = False
print(primes)
