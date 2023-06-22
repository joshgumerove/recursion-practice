def factorial(n):
    if n == 1:
        return n
    return n * factorial(n -1)

print(factorial(5))

def fact(n):
    val = 1
    
    for num in range(1, n + 1):
        print(num)
        val *= num
    return val
        
print(fact(5))