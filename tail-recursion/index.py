def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)

def iterative_1(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

def sum_to_n_tail(n, total = 0):
    if n == 0:
        return total
    return sum_to_n_tail(n -1, total + n)

print(sum_to_n(5))
print(iterative_1(5))
print(sum_to_n_tail(5))

def pow(a, b):
    if b == 0:
        return 1
    return a * pow(a, b -1)

print(pow(2, 4))

def pow_tail(a, b, acc = 1):
    if b == 0:
        return acc
    return (a, b - 1, acc * a)

print(pow(2, 4))

def get_minimum_recursive(arr, i = 0):
    if i == len(arr):
        return float('inf')
    else:
        return min(arr[i], get_minimum_recursive(arr, i + 1))
print(get_minimum_recursive([5, 4, 100, -1, 2]))

    