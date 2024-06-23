# 1, 2반 소웨개, 3반 임베디드, 4반 ai
soft, imvedid, ai, nothing = 0, 0, 0, 0

def a():
    global soft, imvedid, ai, nothing
    cnt = int(input())
    for i in range(cnt):
        grade, classNo, club = map(int, input().split())
        if grade == 1:
            nothing += 1
        elif classNo == 1 or classNo == 2:
            soft += 1
        elif classNo == 3:
            imvedid += 1
        elif classNo == 4:
            ai += 1

a()
print(soft)
print(imvedid)
print(ai)
print(nothing)
