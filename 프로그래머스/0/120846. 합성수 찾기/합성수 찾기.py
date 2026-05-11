def solution(n):
    answer = 0
    for i in range(1, n+1):
        # 소수라면 pass, 아니면 answer += 1 
        # 소수 판별법 > 해당 값 이전의 모든 수를 나누었을때 모든 나머지 값이 0이 아니어야 함
        for j in range(2, i):
            if i % j == 0:
                answer += 1
                break
    return answer