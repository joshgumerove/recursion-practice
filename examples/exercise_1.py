def sum_of_digits(n):
    if n < 10:
        return n
    
    return sum_of_digits(n//10) + n%10

print(sum_of_digits(400))

def count_occurences(arr, num):
    occurences = 0
    
    for occurence in arr:
        if occurence == num:
            occurences += 1
    return occurences

def recurse_count_occurences(arr, num):
    if len(arr) == 0:
        return 0
    occurences = 0
    if num == arr.pop():
        occurences += 1
    return occurences + recurse_count(arr, num)

print(recurse_count_occurences([3, 4, 3, 3, 2, 1, 4, 3], 4))
    
    

