def solution(n, m):
    answer = []
    # 최대 공약수
    for i in range(1, min(n,m)+1):
        if m % i == 0 and n % i == 0:
            max_val = i
    # 최소 공배수
    for j in range(2, 1000000):
        if j % n == 0 and j % m == 0:
            min_val = j
            break
        
    return [max_val, min_val]