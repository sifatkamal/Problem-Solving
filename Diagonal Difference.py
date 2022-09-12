n = int(input())

matrixx = []

index_1 = 0

index_2 = -1

store_1 = 0

store_2 = 0

for i in range(n):
    
    row = input().split(" ")
    
    for i in range(len(row)):
        
        row[i] = int(row[i])
    
    matrixx.append(row)

for i in matrixx:
    
    value_1 =  i[index_1] + store_1
    
    store_1 = value_1
    
    index_1+=1
    
    value_2 = i[index_2] + store_2
    
    store_2 = value_2
    
    index_2-=1
    
final_value = value_2 - value_1

if final_value < 1:
    
    final_value = final_value * -1
    
    print(final_value)
    
else:
    
    print(final_value)
