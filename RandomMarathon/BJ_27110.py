c = int(input())
hu, gan, yang = list(map(int, input().split()))
cnt = 0
if c >= hu :
    cnt += hu
else : 
    cnt += c
if c >= gan :
    cnt += gan
else : 
    cnt += c
if c >= yang :
    cnt += yang
else : 
    cnt += c

print(cnt)