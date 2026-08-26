def solution(n):
    answer = ''
    li = []
    n = str(n)
    for i in range(len(n)):
        li.append(int(n[i]))
    li.sort(reverse=True)
    
    for j in range(len(li)):
        answer += str(li[j])
    answer = int(answer)
    
    return answer