# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
total = 0
last = current = 1
while current < 4000000:
    if current%2 == 0:
        total += current
    last, current = current, last + current
print(total)
