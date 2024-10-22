num = int(input())

odd = 0

while num % 2 == 0:
    num = num // 2
    odd += 1

print(num, odd)