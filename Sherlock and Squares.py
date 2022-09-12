q = int(input())

for i in range(q):
    
    a, b = input().split(" ")
    
    a = int(a)
    
    b = int(b)
    
    listt = []
    
    count = 0
    
    while True:
        
        value = count**2
        
        if value >= a and value <= b:
            
            listt.append(value)
            
        elif value >= b:
            
            break
        
        count+=1
        
    print(len(listt))
