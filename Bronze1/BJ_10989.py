import sys

len_ = int(sys.stdin.readline())
n_list = [0]*10001
for i in range(len_):
    j = int(sys.stdin.readline())
    n_list[j] = n_list[j]+1

for i in n_list:
    if i is 0:
        continue
    print(i) 