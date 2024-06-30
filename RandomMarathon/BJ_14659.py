n = int(input())
print(n)
data = list(map(int, input().split()))
 
height = data[0]
ans = []
count = 0
 
for i in range(1, n):
  if data[i] < height:
    count += 1
  else:
    height = data[i]
    ans.append(count)
    count = 0

ans.append(count)
print(max(ans))