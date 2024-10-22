count = int(input())

for i in range(count):
    n = str(input())
    score = 0
    sum= 0
    for j in n:
        if j == 'O':
            score += 1
        else:
            score = 0
        sum += score
    print(sum)