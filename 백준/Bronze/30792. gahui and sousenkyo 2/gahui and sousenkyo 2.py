#아 쒸발 영어
n = int(input())
m = int(input())
votes = list(map(int, input().split()))
votes.append(m)
votes.sort(reverse=True)
print(votes.index(m)+1)