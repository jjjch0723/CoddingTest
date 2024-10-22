# 시작잔액 정수(-200 ~ 10000)
# 인출 W 입금 D
# 금액 (5 ~ 400)
while True:
    bal, cal, mon = list(map(str, input().split()))
    bal = int(bal)
    mon = int(mon)
    
    if bal == 0 and cal == 'W' and mon == 0:
        break
    
    if cal == 'W':
        if bal - mon < -200:
            print('Not allowed')
        else:
            bal -= mon
            print(bal)
    elif cal == 'D':
        bal += mon
        print(bal)
