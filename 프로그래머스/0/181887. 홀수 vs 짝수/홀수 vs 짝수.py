def solution(num_list):
    answer = 0
    even, odd = 0, 0
    for i in range(0, len(num_list), 2):
        odd += num_list[i]
    for j in range(1, len(num_list), 2):
        even += num_list[j]
    if even > odd :
        answer = even
    else : 
        answer = odd
    return answer