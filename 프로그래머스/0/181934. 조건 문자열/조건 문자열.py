def solution(ineq, eq, n, m):
    comp = ineq+eq
    if comp =='<=':
        return int(n <= m)
    elif comp =='>=':
        return int(n >= m)
    elif comp == '<!':
        return int(n < m)
    else:
        return int(n > m)
    return answer