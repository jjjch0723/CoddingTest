import sys

input = sys.stdin.read
data = input().split()
Q = int(data[0])

results = []

for i in range(1, Q + 1):
    a = int(data[i])
    if a & (a - 1) == 0:
        results.append('1')
    else:
        results.append('0')

print("\n".join(results))
