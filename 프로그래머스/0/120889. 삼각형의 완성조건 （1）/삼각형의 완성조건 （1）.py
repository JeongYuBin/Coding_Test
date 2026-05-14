def solution(sides):
    answer = 0
    # list 총합 - 가장 긴 것 = 두 개의 합
    # 두 개의 합 > 가장 긴 것
    long = max(sides)
    total = sum(sides)
    hap = total - long
    if hap > long :
        answer = 1
    else:
        answer = 2
    return answer