# nombre de page à atteindre

total_page = 5
page_target = 4

def pageCount(n, p):
    
    first_page = 1
    
    result_one = p - first_page
    
    if n % 2 == 0:
        result_two = (n - p + 1) // 2
    else:
        result_two = (n - p) // 2
    
    final_result = min(result_one, result_two)
    
    return final_result
    
print(pageCount(total_page, page_target))
        
    