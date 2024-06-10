querry = int(input())

result = []
for i in range(querry):
    a = int(input())
    
    # 2의 거듭제곱인지 확인
    if a & (a - 1) == 0:
        result.append(1)
    else:
        result.append(0)

# 결과 출력
for i in result:
    print(i)