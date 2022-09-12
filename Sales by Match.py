n = int(input())

socks = input()

socks = socks.split(" ")

socks_2 = list(map(int, socks))

result = 0

while socks_2 != []:
    
    value = socks_2[0]
    
    quantity = socks_2.count(value)
    
    if quantity%2 == 0:
    
        result+=1
    
    socks_2.remove(value)
    
print(result)    
    
    
    
    
