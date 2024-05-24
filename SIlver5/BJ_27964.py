tops_num = int(input())
toppings = list(map(str, input().split()))
cheese_name = set()

for topping in toppings:
    if topping.endswith("Cheese"):
        cheese_name.add(topping)

if len(cheese_name) >= 4 :
    print('yummy')
    #print(len(cheese_name))
else :
    print('sad')
    #print(len(cheese_name))