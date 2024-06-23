# 영어 십라
score = []
for i in range(2) :
    t, f, s, p, c = list(map(int, input().split()))
    t = t * 6
    f = f * 3
    s = s * 2
    p = p * 1
    c = c * 2
    score.append(t+f+s+p+c)

print(score[0], score[1])

