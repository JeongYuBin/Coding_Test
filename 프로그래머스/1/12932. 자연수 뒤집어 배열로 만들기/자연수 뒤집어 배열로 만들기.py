def solution(n):
    buck = []
    answer = []
    n = str(n)
    for i in range(1, len(n)+1):
        buck.append(n[-i])
    for k in range(len(buck)):
        answer.append(int(buck[k]))
    
    return answer