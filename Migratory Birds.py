length = int(input())

listt = input().split(" ")

visited = []

repeatation = {}

count = 0

for i in listt:
    
    count = 0
    
    if i not in visited:
    
        for j in listt:
            
            if i == j:
            
                count+=1
            
        visited.append(i)        
            
        repeatation[i] = count
        
    else:
        
        continue
    
#index = 0

listt_2 = []

maximum = max(repeatation.values())
    
for i in repeatation:
    
    if repeatation[i] == maximum:
        
        listt_2.append(i)

if listt_2 != []:
    
    print(min(listt_2))
    
else:
    
    print("0")
    
    
    
