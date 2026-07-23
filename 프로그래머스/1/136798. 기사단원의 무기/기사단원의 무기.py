# 약수의 개수가 힘 이다.
# 제한수치보다 크면 limit -1 값을 가지기

def solution(number, limit, power):
    answer = 0
    check = [0]*number
    for i in range(1, number+1):
        value = 0
        if i == 1:
            check[i-1] = 1
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                value += 1
                # 약수가 서로 다른 경우 반대쪽 약수도 추가하기
                if j != i // j:
                    value += 1
        check[i-1] = value
    for k in range(number):
        if check[k] > limit:
            check[k] = power
        answer += check[k]
    
    
    return answer