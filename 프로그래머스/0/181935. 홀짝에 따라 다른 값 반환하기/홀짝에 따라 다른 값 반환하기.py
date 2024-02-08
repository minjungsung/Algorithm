def solution(n):
    answer = 0
    if n % 2 == 0:
        for i in range(n,0,-2):
            answer += i * i
    else:
        for i in range(n,0,-2):
            answer += i
    return answer