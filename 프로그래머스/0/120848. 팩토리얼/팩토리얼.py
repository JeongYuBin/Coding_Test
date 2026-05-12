def solution(n):
    answer = 0 
    if 3628800 == n:
        answer = 10
    if 3628800 > n and 362880 <= n:
        answer = 9
    if 362820> n and 40320 <=  n :
        answer = 8
    if 40320 > n and 5040 <= n :
        answer = 7
    if 5040 > n and 720 <= n:
        answer = 6
    if 720 > n and 120 <= n:
        answer = 5
    if 120 > n and 24 <= n:
        answer = 4
    if 24 > n and 6 <= n :
        answer = 3
    if 6 > n and 2 <= n:
        answer = 2
    if 2 > n:
        answer =1 
    return answer