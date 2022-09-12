budget, keyboard_number, disk_number = input().split(" ")

budget = int(budget)

keyboard_number = int(keyboard_number)

disk_number = int(disk_number)

keyboard = input().split(" ")

disk = input().split(" ")

index_1 = 0

index_2 = 0
    
while True:
    
    if index_1 < keyboard_number:
    
        keyboard[index_1] = int(keyboard[index_1])
    
    if index_2 < disk_number:
    
        disk[index_2] = int(disk[index_2])
    
    if index_1 > keyboard_number and index_2 > disk_number:
        
        break
    
    index_1+=1
    
    index_2+=1

result = []

if keyboard_number < disk_number or keyboard_number == disk_number:

    for i in keyboard:
        
        for j in disk:
            
            value = i + j

            if value <= budget:
            
                result.append(value)

            
else:
    
    for i in disk:
        
        for j in keyboard:
            
            value = i + j
            
            if value <= budget:
            
                result.append(value)
            

if result != []:
        
    print(max(result))
    
else:
    
    print("-1")
