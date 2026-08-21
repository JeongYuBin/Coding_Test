def solution(x, n):
    answer = []
    check = x
    for i in range(n):
        answer.append(x)
        x += check
    return answer