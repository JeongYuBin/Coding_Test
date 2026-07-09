def solution(name, yearning, photo):
    answer = []
    dict = {}
    for j in range(len(name)):
        dict[name[j]] = yearning[j]
    
    for i in range(len(photo)):
        score = 0
        for people in photo[i]:
            score += dict.get(people, 0)
        answer.append(score)
            
    return answer