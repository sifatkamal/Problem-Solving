n, k = input().split(" ")

n = int(n)

k = int(k)

listt_1 = []

digit = input()

digit = digit.split(" ")

for i in range(len(digit)):
    
    digit[i] = int(digit[i])

for i in range(len(digit)):
    
    for j in range(len(digit)):
        
        listt_2 = []
        
        value = digit[i] + digit[j]
        
        listt_2.append(digit[i])
        
        listt_2.append(digit[j])
        
        if value % k == 0 and i < j:
            
            listt_1.append(listt_2)       
            
print(len(listt_1))
