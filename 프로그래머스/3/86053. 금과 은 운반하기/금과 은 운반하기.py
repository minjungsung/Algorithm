def solution(a, b, g, s, w, t):
    L,R = 1, 4 * (10**14)
    n = len(g)
    while L <= R:
        T = (L+R)//2
        W,G,S =0,0,0
        for town in range(n):
            if T < t[town]:
                continue
            X = w[town] + ((T - t[town]) // (t[town] * 2)) * w[town]
            G += min(X,g[town])
            S += min(X,s[town])
            W += min(X,g[town] + s[town]) 
            
        if G >= a and S >= b and W >= (a+b):
            R = T-1
        else:
            L = T+1
            
    return L
            