#영어 쉬밸;
n = int(input())
box = list(map(float, input().split()))
boxes = 0
for i in box:
    boxes += i ** 3
j = boxes ** (1/3)
print(f"{j:.6f}")