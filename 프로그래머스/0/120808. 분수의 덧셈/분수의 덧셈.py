import math
def solution(numer1, denom1, numer2, denom2):
    top_num = denom1 * numer2 + denom2 * numer1
    bottom_num = denom1 * denom2
    gcd = math.gcd(top_num, bottom_num)
    
    return [top_num // gcd, bottom_num // gcd]