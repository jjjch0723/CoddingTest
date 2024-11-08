def solution(myString, pat):
    answer = 1
    myString_ = myString.replace("A", "C").replace("B", "A").replace("C", "B")
    
    if pat in myString_:
        return answer
    else :
        answer = 0
        return answer