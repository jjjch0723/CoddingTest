delivery = int(input())
cnt = 0

while delivery >= 0 :
    if delivery % 5 == 0:
        cnt += delivery / 5
        print(int(cnt))
        break
    delivery -= 3
    cnt += 1
else :
    print(-1)