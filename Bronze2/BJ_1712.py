a, b, c = map(int, input().split())

if b >= c : 
    print(-1)
else :
    cal = (a // (c - b))+1
    print(cal)