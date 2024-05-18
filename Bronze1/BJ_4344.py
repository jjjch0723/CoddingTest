roop = int(input())

per_list = []
for i in range(0, roop):
    w = list(map(int, input().split()))
    s_list_num = w[0]
    s_list = w[1:len(w)]

    s_list_avg = sum(s_list)/s_list_num

    cnt = 0
    for j in s_list :
        if j > s_list_avg :
            cnt += 1

    per = (cnt/s_list_num)*100
    per_list.append(per)

for i in range(roop):
    print("{:.3f}".format(per_list[i]), '%')
