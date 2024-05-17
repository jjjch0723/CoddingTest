w = input().upper()
w_l = list(set(w))
lst = []
a = ''

for i in w_l:
    count = w.count(i)
    lst.append(count)

if lst.count(max(lst)) > 1:
    a = '?'
else:
    a = w_l[lst.index(max(lst))]

print(a)