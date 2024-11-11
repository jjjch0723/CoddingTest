def solution(myString):
    a = []
    myString = list(map(str, myString.split('x')))
    for i in myString:
        a.append(len(i))
    return a