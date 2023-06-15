# note how created two stacks

def fact(n):
    prod = 1
    while n > 0:
        prod *= n
        n -= 1
    return prod

print(fact(5))

def nb_divisors(n):
    count = 0
    i = 1   
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

print(nb_divisors(6))

def divisors2(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

print(divisors2(6))

def recursive_div(n, count=0, i=1):
    if i > n:
        return count
    if n % i == 0:
        count += 1
    return recursive_div(n, count, i + 1)

print(recursive_div(6))

def min_value(arr):
    min_value = arr[0]
    for val in arr:
        if val < min_value:
            min_value = val
    return min_value

print(min_value([5, 2, 4, 9, 10, -5, 100]))

def get_min(arr):
    min_val = float('inf')
    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val

print(get_min([5, 2, 4, 9, 10, -5, 100]))
        
def get_min_recursive(arr, i=0, min_val=float('inf')):
    if i >= len(arr):
        return min_val
    if arr[i] < min_val:
        min_val = arr[i]
    return get_min_recursive(arr, i + 1, min_val)

print(get_min_recursive([5, 2, 4, 9, 10, -5, 100]))

def contains_value(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return True
    return False

print(contains_value([20, 30, 40, 50], 40))
print(contains_value([20, 30, 40, 50], 60))

def contains_value_recursive(arr, value, i=0):
    if i >= len(arr):
        return False
    if arr[i] == value:
        return True
    return contains_value_recursive(arr, value, i + 1)

print(contains_value_recursive([20, 30, 40, 50], 40))
print(contains_value_recursive([20, 30, 40, 50], 60))

    

