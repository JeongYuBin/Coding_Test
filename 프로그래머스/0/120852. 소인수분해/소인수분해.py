# def solution(n):
#     answer = []
#     for i in range(2, n+1):
#         while True:
#             q = n % i 
#             if q != 0:
#                 break
#             else: 
#                 n = n // i
#                 answer.append(i)
#     answer = list(set(answer)) # 중복 제거 
#     return answer


def solution(n):
    answer = []
    for i in range(2, n+1):
        if n % i == 0:
            answer.append(i)
            while n % i == 0:
                n //= i
    return answer