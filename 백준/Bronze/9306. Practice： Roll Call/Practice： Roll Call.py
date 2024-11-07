n = int(input())
names = []
for i in range(0, n*2):
    names.append(input())

for j in range(0, n):
    print(f"Case {j+1}: {names[j*2+1]}, {names[j*2]}")