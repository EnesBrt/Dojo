# Sales by matches

socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]
num = 9

def sockMerchant(n, ar):
    socks_count = {}
    length = len(ar)
    
    if length == n:
        for x in ar:
            if x in socks_count:
                socks_count[x] += 1
            else:
                socks_count[x] = 1
        
        paired_socks = [value for value in socks_count.values() if value > 1]
        count_paires = [n // 2 for n in paired_socks]
        
        result = 0
        for  y in count_paires:
            result = result + y 
        
            
    return result
    
print(sockMerchant(num, socks))
            
        
    