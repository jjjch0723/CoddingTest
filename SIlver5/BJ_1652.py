# n = int(input())
# room = []
# w_lie, h_lie = 0, 0

# for i in range(n):
#     room.append(input())

# for i in range(n):
#     lie_cnt = 0
#     for j in range(n):
#         if room[i][j] == '.':
#             lie_cnt += 1
#         else : 
#             if lie_cnt >= 2:
#                 w_lie += 1
#             lie_cnt = 0
#     if lie_cnt >= 2:
#         w_lie += 1

# for j in range(n):
#     lie_cnt = 0
#     for i in range(n):
#         if room[i][j] == '.':
#             lie_cnt += 1
#         else : 
#             if lie_cnt >= 2:
#                 h_lie += 1
#             lie_cnt = 0
#     if lie_cnt >= 2:
#         h_lie += 1

# print(w_lie, h_lie)
n = int(input())
room=[]
w_lie, h_lie = 0, 0
for i in range(n):
    room.append(input())
for width in room :
    beds = width.split('X')
    for bed in beds :
        if(len(bed)) >= 2:
            w_lie += 1

for heigth in room:
    height_ = ''.join(room[width][heigth] for i in range(n))
    beds = height_.split('X')
    for bed in beds:
        if len(bed) >= 2:
            h_lie += 1

print(w_lie, h_lie)
