def solution(num_list):
    answer = 0
    num1 = 0
    num2 = 0
    for i in range(len(num_list)):
        if (num_list[i] % 2):
            num1 = num1 * 10 + num_list[i]
        else:
            num2 = num2 * 10 + num_list[i]
    return num1 + num2