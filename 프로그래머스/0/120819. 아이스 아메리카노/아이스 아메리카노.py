def solution(money):
    jan = money // 5500
    remain = money % 5500
    answer = [jan, remain]
    return answer