def solution(spell, dic):
    answer = 0
    for word in dic:  # word = sod
        if sorted(word) == sorted(spell):
            answer = 1
            break
        else : 
            answer = 2
    return answer