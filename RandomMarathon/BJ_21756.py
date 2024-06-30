n = int(input())
n_arr = list(range(1, n + 1))

while len(n_arr) > 1:
    n_arr1 = []
    for i in range(len(n_arr)):
        if(i + 1) % 2 == 0:
            n_arr1.append(n_arr[i])
    n_arr = n_arr1

print(n_arr[0])