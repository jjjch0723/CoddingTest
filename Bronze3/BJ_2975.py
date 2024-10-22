# 시작잔액 정수(-200 ~ 10000) bal
# 인출 W 입금 D cal
# 금액 (5 ~ 400) mon
while True :

    bal, cal, mon = list(map(str, input().split()))
    bal = int(bal)
    mon = int(mon)

    if bal == 0 and cal == 'W' and mon == 0 :
        break

    if cal == 'W':
        if mon - bal < 200:
            bal = bal - mon
            print(bal)
        else :
            print('not allowed')
    elif cal == 'D':
        bal = bal + mon
        print(bal)