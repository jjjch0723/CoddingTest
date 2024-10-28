n = int(input())
for i in range(1, n + 1):
    print("*"*i + " "*((n-i)*2) + "*"*i)
for j in range(n-1, 0, -1):
    print("*"*j + " "*((n-j)*2) + "*"*j)