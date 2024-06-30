n = int(input())
names = []
p = []
for i in range(n):
    names.append(input())

for i in range(len(names[0])):
    cur_char = names[0][i]
    match = True
    
    for j in range(1, n):
        if names[j][i] != cur_char :
            match = False
            break

    if match:
        p.append(cur_char)
    else:
        p.append("?")

print("".join(p))