def solution(n):
    answer = 0
    for i in range(1, n):
        if n // i == i and n % i == 0:
            answer = 1
            break
        else:
            answer = 2
    return answer