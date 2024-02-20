def solution(number):
    answer = 0
    arr = list(number.strip())
    return sum(int(i) for i in arr)%9
    