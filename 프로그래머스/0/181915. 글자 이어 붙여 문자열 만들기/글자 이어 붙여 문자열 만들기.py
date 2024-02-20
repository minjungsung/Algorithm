def solution(my_string, index_list):
    answer = ''
    dic = {}
    string_arr=list(my_string.strip())
    for i,c in enumerate(string_arr):
        dic[i] = c
    for i in index_list:
        answer += dic[i]
    return answer