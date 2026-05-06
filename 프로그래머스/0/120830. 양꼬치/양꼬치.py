def solution(n, k):
    service = n // 10
    k = k - service 
    answer = n*12000 + 2000*k
    
    return answer