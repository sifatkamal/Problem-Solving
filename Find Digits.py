sample = int(input())

for j in range(sample):

    n = input()
    
    listt = list(n)
    
    n = int(n)
    
    listt = list(map(int, listt))
    
    count = 0
    
    for i in listt:
        
        if i == 0:
            
            continue
        
        elif n % i == 0:
            
            count+=1
            
        else:
            
            continue
        
    print(count)