def solution(cards1, cards2, goal):
    answer = "Yes"
    one = 0
    two = 0 
    for g in goal:
        if one < len(cards1) and g == cards1[one]:
            one += 1
        elif two < len(cards2) and g == cards2[two]:
            two += 1
        else:
            answer = "No"   
    return answer