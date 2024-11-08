def solution(num_list, n):
    answer=[]
    for j in range(n, len(num_list)):
        answer.append(num_list[j])
    for i in range(0, n):
        answer.append(num_list[i])
    return answer