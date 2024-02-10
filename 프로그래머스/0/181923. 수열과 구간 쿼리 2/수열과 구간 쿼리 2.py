import numpy
def solution(arr, queries):
    arr = numpy.array(arr)
    answer = []
    for query in queries:
        sub = arr[query[0]:query[1] + 1]
        sub = sub[sub > query[2]]
        if len(sub) == 0:
            answer.append(-1)
        else:
            answer.append(int(numpy.min(sub)))
    return answer