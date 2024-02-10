import numpy

def solution(num_list):  
    val1 = sum(num_list)**2
    val2 = numpy.prod(num_list)
    print(val1, val2)
    if val2 < val1:
        return 1
    elif val2 > val1:
        return 0
    