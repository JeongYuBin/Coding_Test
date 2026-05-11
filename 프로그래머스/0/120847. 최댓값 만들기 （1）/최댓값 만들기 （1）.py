def solution(numbers):
    answer = 0
    numbers.sort(reverse=False)
    answer = numbers[-1] * numbers[-2]
    return answer