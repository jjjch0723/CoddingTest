def solution(arr1, arr2):
    n = 0
    a = len(arr1); b = len(arr2);
    if a > b : 
        n = 1
    elif a < b:
        n = -1
    else :
        n = 1
        a_ = sum(arr1); b_ = sum(arr2);
        if a_ < b_:
            n = -1
        elif a_ == b_:
            n = 0
    return n