import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    num = (numer1 * denom2) + (numer2 * denom1)
    den = denom1 * denom2
    gcd = math.gcd(den, num)
    answer = [num // gcd, den // gcd]
    return answer