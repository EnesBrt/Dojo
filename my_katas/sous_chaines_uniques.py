# Sous-chaînes Uniques

string  = "abcabc"

def unique_substrings(s, n):
    
    letters  = []
    sub_strings= []
    
    for x in range(len(s) - n + 1):
        for y in range(x, x + n):
            letters.append(s[y])
            
    for z in range(0, len(letters), n):
        group = "".join(letters[z:z+n])
        if group not in sub_strings:
            sub_strings.append(group)
        
            
    return sub_strings
        
        
print(unique_substrings(string, 3))