# Find the largest palindrome made from the product of two 3 digit numbers.
def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True

large = spec = 0
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        spec = i * j
        if is_palindrome(spec) and (spec > large):
            large = spec

print(large)
