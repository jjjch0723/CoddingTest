## 아 모르겠다 내가 작성한 로직이 맞는거 같은데

n = int(input())
team_a = list(map(int, input().split()))
team_b = list(map(int, input().split()))

max_streak = 0
current_streak = 0
current_winner = None

for i in range(n):
    move_a = team_a[i]
    move_b = team_b[i]

    if (move_a == 1 and move_b == 3) or (move_a == 2 and move_b == 1) or (move_a == 3 and move_b == 2):
        winner = 'A'
    elif move_a == move_b:
        winner = 'B'
    else:
        winner = 'B'

    if winner == current_winner:
        current_streak += 1
    else:
        current_streak = 1
        current_winner = winner
    max_streak = max(max_streak, current_streak)

print(max_streak)