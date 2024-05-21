def self_num(a):
    sel_n = list(str(a))
    result = 0
    for i in range(len(sel_n)):
        result = result + int(sel_n[i])
    result = result + int(a)
    return result
result = set()
for i in range(10001):
    result.add(self_num(i))
for j in range(10001):
    if j not in result:
        print(j)