def solution(numbers, hand):
    answer = ''
    # 각 번호별 위치 
    loc = {1: [1,1], 2: [1,2], 3: [1,3], 4:[2,1], 5:[2,2], 6:[2,3], 7:[3,1], 8:[3,2], 9:[3,3], 0: [4,2]}
    l_point = [4,1]
    r_point = [4,3]
    
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            l_point = loc[num]
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            r_point = loc[num]
        else:
            num_point = loc[num]
            l_cha = abs(num_point[0]-l_point[0]) + abs(num_point[1] - l_point[1])
            r_cha = abs(num_point[0]-r_point[0]) + abs(num_point[1] - r_point[1])
            if l_cha > r_cha:
                answer += 'R'
                r_point = loc[num]
            elif l_cha < r_cha:
                answer += 'L'
                l_point = loc[num]
            else:
                if hand == "right":
                    answer += 'R'
                    r_point = loc[num]
                else:
                    answer += 'L'
                    l_point = loc[num]
    return answer


# def solution(numbers, hand):
#     answer = ''
#     # 각 호별 위치
#     loc = {1: [4, 1], 2:[4, 2], 3:[4, 3], 4:[3, 1], 5:[3,2], 6:[3,3], 7: [2, 1], 8:[2, 2], 9: [2,3], 0: [1,2]}
    
#     L_point = [1, 1]  # 왼손 시작
#     R_point = [1, 3]  # 오른손 시작
    
#     for i in numbers:
#         if i ==1 or i == 4 or i == 7:
#             answer += 'L'
#             L_point = loc[i]
#         elif i == 3 or i == 6 or i ==9:
#             answer += 'R'
#             R_point = loc[i]
#         else: 
#             value = loc[i]
#             L_cha = abs(value[0] - L_point[0]) + abs(value[1] - L_point[1])
#             R_cha = abs(value[0] - R_point[0]) + abs(value[1] - R_point[1])
            
#             if L_cha < R_cha:
#                 answer += 'L'
#                 L_point = loc[i]
#             elif L_cha > R_cha:
#                 answer += 'R'
#                 R_point = loc[i]
#             else:
#                 if hand == 'right':
#                     answer += 'R'
#                     R_point = loc[i]
#                 else:
#                     answer += 'L'
#                     L_point = loc[i]
      
#     return answer