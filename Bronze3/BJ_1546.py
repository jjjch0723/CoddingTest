cnt = int(input())
subs = list(map(int, input().split()))
s_max = max(subs)
news = []
k = 0
for i in range(0, cnt) :
    news.append(subs[i]/s_max*100)
for j in range(0, cnt) :
    k += news[j]

print(k/cnt)