# 가장 큰 수부터 상자에 담기 
# 먼저 score를 정렬해서 큰 수부터 빼기

def solution(k, m, score):
    answer = 0
    value = [] 
    score = sorted(score, reverse= True)
    for i in range(0,len(score),m):
        if i+m <= len(score):
            value = score[i:i+m]
            check = value[-1]*m
            answer += check
    return answer  


