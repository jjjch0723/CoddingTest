#영어 쉬부렝ㅁ
cnt = int(input())
election_List = []
for i in range(cnt):
    election_List.append(int(input()))

carlos = election_List[0]
if carlos >= max(election_List[1:]):
    print('S')
else : 
    print('N')