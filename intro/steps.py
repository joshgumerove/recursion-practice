# def factorial(n):
#     if n == 1: # base case
#         return n
#     else:
#         return n * factorial(n -1) # recursive call

# print(factorial(5))

# def fib(n):
#     if n <= 1: # base case
#         return n
#     else:
#         return fib(n-1) + fib(n -2) # recursive call(s)
    
# print(fib(10))


# # def merge_sort(arr):
# #     if len(arr) <= 1:
# #         return arr
# #     else:
# #         mid = len(arr)//2 # so does not return a float
# #         left = arr[:mid]
# #         right = arr[mid:]
# #         left = merge_sort(left)
# #         right = merge_sort(right)
# #         return merge_sorted_arr(left, right)

# def func1():
#     print('i am the first function')
#     func2()
#     print('i am the first function')

# def func2():
#     print('i am THE SECOND function')

# func1()

def func(n):
    if n == 1:
        print(1) # do not need to return becaue will just print if 1 and never make it to else recursive call
    else:
        print(n, "first call")
        func(n-1)
        print(n, "second call")

func(4)

def func2(n):
    if n == 1:
        print(1)
    else:
        func2(n-1)
        print(n, "what")
        func2(n -1) # note the order this runs in
        

func2(4)

def is_prime(n, i=2):
    if i == n:
        return True # base case that ends loop
    elif n % i == 0:
        return False # base case that may occur and end loop earlier
    else:
        print(n, " what is it", i)
        return is_prime(n, i + 1)

print(is_prime(53))

# 2 --> 1 print(1) print(2 what)
# 2 (second) --> print(1)
# 3 --> print(3)
# 3(second) --> print(1) print(2 what)
# 4 --> print (4 what)
# 4 (second) --> print(1) print(2 what)
