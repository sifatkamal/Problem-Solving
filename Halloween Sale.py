a = input()

p, d, m, s = a.split(" ")

p = int(p)

d = int(d)

m = int(m)

s = int(s)

summ = 0

count = 0

value  = m

while summ <= s and value >= m:
    
    summ = p + summ
    
    if summ > s:
        
        break
    
    p = p - d
    
    if p <= m:
        
        p = m
    
    count+=1
    
    value = s - summ
    
print(count)
