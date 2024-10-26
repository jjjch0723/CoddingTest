# 아 사전순

n = int(input())

names = []
fnames = []
count = []

for i in range(n):
    names.append(input())

for name in names:
    fnames.append(name[0])

fnames_ = set(fnames)

for j in fnames_:
    if fnames.count(j) > 4:
        count.append(j)

if len(count) > 0:
    print(''.join(sorted(count)))
else :
    print("PREDAJA")