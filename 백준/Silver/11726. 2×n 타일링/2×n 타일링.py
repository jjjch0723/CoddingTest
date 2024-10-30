n = int(input())

side = [0] * 1001

side[1] = 1
side[2] = 2
for i in range (3, n+1) :
    side[i] = (side[i-1] + side[i-2]) % 10007

print(side[n])
