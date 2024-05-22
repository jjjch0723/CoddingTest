# from collections import Counter as c
# nums = list(map(int, input().split()))
# num_a = []
# num_b = []

# for i in range(len(nums)) :
#     for j in range(1,nums[i]+1):
#         if nums[i] % j == 0:
#             num_a.append(nums[i]//j)

# cnt = c(num_a)
# num_a = [num for num in num_a if cnt[num] > 1]
# num_a.sort()
# print(num_a[-1])
# 재미로 해본 최대공약수 계산법
# 그냥 유클리드 호제법쓰자 ㅋㅋ

nums = list(map(int, input().split()))
num1 = nums[0]
num2 = nums[1]

def gcd_(num1, num2):
    while(num2>0):
        num1, num2 = num2, num1 % num2
    return num1

gcd = gcd_(num1, num2)
lcd = (num1 * num2) // gcd_(num1, num2)

print(gcd, lcd)