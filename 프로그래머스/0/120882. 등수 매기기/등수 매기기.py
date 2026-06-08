def solution(score):
    answer = []
    avg = [] 
    for a, b in score:
        avg.append((a+b)/2)
    for i in range(len(avg)):
        rank = 1
        for j in range(len(avg)):
            if avg[i] < avg[j]:
                rank += 1
        answer.append(rank)
    
    return answer