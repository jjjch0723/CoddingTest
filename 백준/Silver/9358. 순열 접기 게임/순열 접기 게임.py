import math

count = int(input())

for t in range(count):
    num = int(input())
    seq = list(map(int, input().split()))

    while num > 2:
        new_seq = []
        for i in range(num // 2):
            new_seq.append(seq[i] + seq[num - 1 - i])

        if num % 2 == 1:
            new_seq.append(seq[num // 2] * 2)

        seq = new_seq
        num = math.ceil(num / 2)

    if seq[0] > seq[1]:
        print(f"Case #{t+1}: Alice")
    else:
        print(f"Case #{t+1}: Bob")
