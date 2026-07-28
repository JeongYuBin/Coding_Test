# a : 마트에 줘야하는 빈 병
# b : 마트가 주는 콜라병
# n : 내가 가지고 있는 빈 병

def solution(a, b, n):
    answer = 0
    while n >= a:
        receive = n // a * b
        # 받은 병 추가
        answer += receive
        n = n%a + receive
    return answer