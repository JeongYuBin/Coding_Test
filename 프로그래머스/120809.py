# https://school.programmers.co.kr/learn/courses/30/lessons/120809
# 배열 두 배 만들기

def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
        
    return numbers

# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         answer.append(numbers[i] * 2)
        
#     return answer