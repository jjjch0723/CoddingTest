score = list(map(int, input().split()))
team_num = int(input())
teamMem = 3
team_score = []
for teams in range(team_num):
    s = 0
    for i in range(teamMem):
        oneHand, noLook, pone = list(map(int, input().split()))
        s += (oneHand * score[0]) + (noLook * score[1]) + (pone * score[2])
    team_score.append(s)

print(max(team_score))