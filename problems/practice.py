# Write a function that finds all numbers between 1 and 1000 where the digital root equals the number of digits in the original number.
def root(x):
    if x < 10:
        return x
    str_list = list(str(x))
    num_list = [int(s) for s in str_list]
    return root(sum(num_list))

result = []
for i in range(1, 1000):
    if len(str(i)) == root(i):
        result.append(i)
print(result)