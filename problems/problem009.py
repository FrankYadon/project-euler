# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
def square_check(x, y, z):
    return (x**2) + (y**2) == (z**2)

for i in range(334):
    for j in range (i + 1, 1000 - i):
        k = 1000 - i - j
        if (k > j) and square_check(i, j, k):
            print(i * j * k)
            exit()
