def solution(name, yearning, photo):
    answer = []
    dict = {}
    for j in range(len(name)):
        dict[name[j]] = yearning[j]
    
    for i in range(len(photo)):
        score = 0
        for people in photo[i]:
            if people in dict:
               score += dict[people]
        answer.append(score)
            
    return answer