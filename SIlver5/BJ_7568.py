cnt = int(input())
peoples = []
for i in range(cnt):
    peoples.append(list(map(int, input().split())))

rank = [1] * cnt

for i in range(cnt):
    for j in range(cnt):
        if i != j:
            if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1] :
                rank[i] += 1

print(" ".join(map(str, rank)))