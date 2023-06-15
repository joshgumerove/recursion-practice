# note how created two stacks

def fact(n):
    prod = 1
    while n > 0:
        prod *= n
        n -= 1
    return prod

print(fact(5))
