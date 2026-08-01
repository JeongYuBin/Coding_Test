def solution(price, money, count):
    answer = 0
    total = 0
    for i in range(1, count+1):
        pay = i*price
        total += pay
    answer = money - total
    if answer>=0:
        return 0
    else:
        answer = abs(answer)

    return answer