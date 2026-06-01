def solution(dots):
    answer = 0
    #1. (1,2), (3,4)
    x_1_1 = dots[0][0] - dots[1][0]
    x_1_2 = dots[2][0] - dots[3][0]
    y_1_1 = dots[0][1] - dots[1][1]
    y_1_2 = dots[2][1] - dots[3][1]
    
    if y_1_1 / x_1_1 == y_1_2 / x_1_2:
        answer = 1
    
    #2. (1,3), (2,4)
    x_2_1 = dots[0][0] - dots[2][0]
    x_2_2 = dots[1][0] - dots[3][0]
    y_2_1 = dots[0][1] - dots[2][1]
    y_2_2 = dots[1][1] - dots[3][1]
    
    if y_2_1 / x_2_1 == y_2_2 / x_2_2: 
        answer = 1
    
    #3. (1,4), (2,3)
    x_3_1 = dots[0][0] - dots[3][0]
    x_3_2 = dots[1][0] - dots[2][0]
    y_3_1 = dots[0][1] - dots[3][1]
    y_3_2 = dots[1][1] - dots[2][1]
    
    if y_3_1 / x_3_1 == y_3_2 / x_3_2:
        answer = 1
    return answer