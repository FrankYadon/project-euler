# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
n = 100
sum_squares = (n * (n + 1) * (2 * n + 1)) / 6
square_sums = (n * (n + 1) / 2) ** 2
print (square_sums - sum_squares)