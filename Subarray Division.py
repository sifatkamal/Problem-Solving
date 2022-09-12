a = int(input())

b = input().split(" ")

c, d = input().split(" ")

c = int(c)

d = int(d)

b = list(map(int, b))

value = []

def Subarray_Division(b):

    lists = [[]]
    
    for i in range(len(b) + 1):

        for j in range(i):
            
            if len(b[j: i]) == d:

                lists.append(b[j: i])
    
    for i in lists:
        
        summ = 0
        
        for j in i:
        
            result = j + summ
            
            summ = result
        
        if summ == c:
        
            value.append(summ)
            
    return len(value)

print(Subarray_Division(b))

