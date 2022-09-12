n = int(input())

p = int(input())

division = n//2

#1st page

if p <= division:
    
    if p == 1:
        
        print("0")
    
    elif p%2 == 0:
        
        page = p//2
        
        print(page)
        
    else:
        
        p = p - 1
        
        page = p//2
        
        print(page)

#Last Page
        
elif p >= division:
    
    if p%2 == 0:
        
        value = n - p
        
        page = value // 2
        
        print(page)
        
    else:
        
        p = p - 1
        
        value = n - p
        
        page = value // 2
        
        print(page)
        
else:
    
    print("0")
