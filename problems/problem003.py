# What is the largest prime factor of the number 600851475143?
target = 600851475143
curr = 3
while curr < target:
    while (target%curr == 0):
        target = target / curr
    curr += 2
print(target)