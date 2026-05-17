def solution(order):
    answer = 0
    while order > 0:
        a = order % 10
        if a == 3 or a == 6 or a == 9:
            answer += 1
        order //= 10
    return answer