def solution(strArr):
    answer = []
    for i, char in enumerate(strArr) :
        if i % 2 == 0:
            answer.append(char.lower())
        else :
            answer.append(char.upper())
    return answer