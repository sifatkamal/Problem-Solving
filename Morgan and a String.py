def lex(a, b):
    
    length_a = len(a)
    
    length_b = len(b)
    
    a = a + "a"
    
    b = b + "a"
    
    count_1 = 0
    
    count_2 = 0
    
    result = ""
    
    while (count_1 != length_a and count_2 != length_b):
        
        if a[count_1:] < b[count_2:]:

            result = result+a[count_1]
            
            count_1+=1

        else:

            result = result + b[count_2]
            
            count_2+=1
            
    result = result + a[count_1: -1] + b[count_2: -1]
    
    print(result)
    

T = int(input())

for i in range(T):
    
    a = input()
    
    b = input()
    
    lex(a, b)