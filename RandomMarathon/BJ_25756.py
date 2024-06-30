# 아오 메쌤!!!
def AO_MaSSAM(N, potions):
    V = 0.0  # 초기 방무 0
    bangmu = []

    for A_i in potions:
        V = 1 - (1 - V) * (1 - A_i / 100.0)
        bangmu.append(round(V * 100, 6))
    
    return bangmu

cnt = int(input())
potions = list(map(int, input().split()))

bangmu = AO_MaSSAM(cnt, potions)

for i in bangmu:
    print(i)