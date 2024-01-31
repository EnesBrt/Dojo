# Caesar cipher
import string 


def caesarCipher(s, k):
    
    result = ''
    
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    
    for n in s:
        if n.islower():
            index = lower.index(n)
            result += lower[(index + k) % 26]
        elif n.isupper():
                index = upper.index(n)
                result += upper[(index + k) % 26]
        else:
            result += n
        
    
    return result
    
print(caesarCipher('hello', 2))
