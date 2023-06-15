# without memoization --> repeating function calls uselessly
# using memoization --> produces a smaller recursion tree (reduces time complexity)

def fib_memoized(n, lookup={}):
    key = str(n)
    if key in lookup:
        return lookup[key]
    if n <= 1:
        lookup[key] = n
        return lookup[key]
    
    ans = fib_memoized(n - 1) + fib_memoized(n -2)
    lookup[key] = ans
    print(lookup)
    print(ans)
    return ans

print(fib_memoized(10))