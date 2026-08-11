def solution(numbers, hand):
    answer = ''
    # 각 호별 위치
    loc = {1: [4, 1], 2:[4, 2], 3:[4, 3], 4:[3, 1], 5:[3,2], 6:[3,3], 7: [2, 1], 8:[2, 2], 9: [2,3], 0: [1,2]}
    
    L_point = [1, 1]  # 왼손 시작
    R_point = [1, 3]  # 오른손 시작
    
    for i in numbers:
        if i ==1 or i == 4 or i == 7:
            answer += 'L'
            L_point = loc[i]
        elif i == 3 or i == 6 or i ==9:
            answer += 'R'
            R_point = loc[i]
        else: 
            value = loc[i]
            L_cha = abs(value[0] - L_point[0]) + abs(value[1] - L_point[1])
            R_cha = abs(value[0] - R_point[0]) + abs(value[1] - R_point[1])
            
            if L_cha < R_cha:
                answer += 'L'
                L_point = loc[i]
            elif L_cha > R_cha:
                answer += 'R'
                R_point = loc[i]
            else:
                if hand == 'right':
                    answer += 'R'
                    R_point = loc[i]
                else:
                    answer += 'L'
                    L_point = loc[i]
      
    return answer