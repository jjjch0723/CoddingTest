cnt = int(input())

check_list = []

for i in range(cnt) : 
    j = int(input())
    if(j % 2 == 0) :
        check_list.append("even")
    else : 
        check_list.append("odd")

for num in check_list:
    print(num)