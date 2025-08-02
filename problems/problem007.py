# What is the 10001st prime number?
primes = []
lower_bound = 2
upper_bound = 120000
test = list(range(lower_bound, upper_bound))
for t in test:
    if t != 0:
        primes.append(t)
        num = t
        while num < upper_bound:
            num += t
            if num in test:
                test[test.index(num)] = 0
print(primes[10000])
