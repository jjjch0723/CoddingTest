n = int(input())
judges = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    judges.append((age, name))

judges.sort(key=lambda x : x[0])

for i in judges:
    print(str(i[0])+' '+i[1])