s = input()

s = s.split(":")

value = int(s[0])

index_1 = 0

index_2 = 0

last = s[2]

last = list(last)

store = s[0]

for i in last:
    
    if i == "P":
        
        if value < 12:
            
            value_2 = value + 12
            
            print(value_2, end = ":")
            
        else:    
        
            print(s[0], end = ":")
            
        print(s[1], end = ":")
            
        print(last[0], end = "")
        
        print(last[1], end = "")
        
        break
    
    elif i == "A":
        
        if store == "12":
            
            print("00", end = ":")
            
        else:
            
            print(s[0], end = ":")
            
        print(s[1], end = ":")
            
        print(last[0], end = "")
        
        print(last[1], end = "")
        
        break
        
