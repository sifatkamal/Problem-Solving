a = input()

items, decline = a.split(" ")

items = int(items)

decline = int(decline)

price = input()

price = price.split(" ")

price = list(map(int, price))

charge = int(input())

total = sum(price)

shared = (total - price[decline])//2

remain = charge - shared

if remain == 0:
    
    print("Bon Appetit")
    
else:    

    print(remain)
