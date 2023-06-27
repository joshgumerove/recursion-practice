# Parameters:
#  s: str
# return type: str

def reverse(s, i = 0):
    if i == len(s) -1:
        return s[i]
    val =  reverse(s, i + 1) + s[i]
    return val

print(reverse("josh"))
print(reverse("inside code"))

def reverse_recurse(s):
    if s == "":
        return ''
    return reverse_recurse(s[1:]) + s[0]
print(reverse_recurse("josh"))