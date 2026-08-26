import math

def solution(n):
    answer = -1
    sq = math.sqrt(n)
    for i in range(1, int(sq+1)):
        if i**2 == n:
            answer = (i+1)**2
    
    
    return answer