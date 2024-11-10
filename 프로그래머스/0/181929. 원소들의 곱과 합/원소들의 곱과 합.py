def solution(num_list):
    answer = 0
    i, j = 1, sum(num_list) ** 2
    for i_ in num_list:
        i *= i_
    
    if i > j :
        answer = 0
    else :
        answer = 1
    return answer