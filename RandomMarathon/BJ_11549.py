#영어 쉬밸;
tea = int(input())
blind = list(map(int, input().split()))
cnt = 0
for i in blind :
    if i == tea :
        cnt += 1

print(cnt)