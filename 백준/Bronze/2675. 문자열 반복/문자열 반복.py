cnt = int(input())
for i in range(cnt):
    n, chars = input().split()
    chars = list(chars)
    for j in range(len(chars)):
        print(chars[j]* int(n), end="")
    print()