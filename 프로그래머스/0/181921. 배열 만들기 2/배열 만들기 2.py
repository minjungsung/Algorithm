def solution(l, r):
    answer = []
    for i in range(l, r+1):
        tempStr = str(i).replace('5','').replace('0','')
        if (len(tempStr)==0):
            answer.append(i)
    if (len(answer)==0):
        return [-1]
    return answer