def solution(n, control):
    answer = 0
    for i in range(len(control)):
        i = control[i]
        if i=='w':
            n += 1
        elif i =='s':
            n -= 1
        elif i =='d':
            n += 10
        elif i =='a':
            n -= 10
    return n