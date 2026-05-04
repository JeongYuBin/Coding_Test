def solution(numbers):
    result = 0 
    for i in range(len(numbers)):
        result += numbers[i]
    answer = result / len(numbers)
    return answer