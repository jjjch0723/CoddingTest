triangle = []

def get_input():
    triangle.append(list(map(int, input().split())))

while True:
    get_input()
    if triangle[-1] == [0, 0, 0]:
        break

for i in triangle:
    if i == [0, 0, 0]:
        continue
    i.sort()
    sqaure = i[2] ** 2
    sqaure_ = i[0]**2 + i[1]**2
    if sqaure == sqaure_ :
        print('right')
    else : 
        print('wrong')