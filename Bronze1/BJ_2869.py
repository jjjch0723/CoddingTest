import math as m
a, b, v = list(map(int, input().split()))

result = int(m.ceil(float((v-b)/(a-b))))
print(result)