def solution(arr, k):
    return [i * k if k % 2 == 1 else i + k for i in arr]
