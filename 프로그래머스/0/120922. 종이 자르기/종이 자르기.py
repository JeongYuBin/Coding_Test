# M, N 중에서 큰 값 -1 + M, N 중에서 큰 값
def solution(M, N):
    a = max(M,N)
    b = min(M, N)
    
    answer = (a-1) + a*(b-1)
    return answer
    