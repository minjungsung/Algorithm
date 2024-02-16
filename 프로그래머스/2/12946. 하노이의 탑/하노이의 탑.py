from typing import List

def solution(n):
    answer = hanoi(n, 1, 3, 2,[])
    
    return answer

def hanoi(n:int, fm:str, to:str, other:str, answer:List):
    if n == 0:
        return
    hanoi(n-1, fm, other, to,answer)
    answer.append([fm, to])
    hanoi(n-1, other, to, fm,answer)
    return answer