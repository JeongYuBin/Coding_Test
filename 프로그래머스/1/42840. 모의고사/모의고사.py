# 1번 사용자 반복 : 1 2 3 4 5   -> 5개
# 2번 사용자 반복 : 2 1 2 3 2 4 2 5 -> 8개
# 3번 사용자 반복 : 3 3 1 1 2 2 4 4 5 5 -> 10개 

def solution(answers):
    answer = []
    fir_dict = {0:1, 1:2, 2:3, 3:4, 4:5}
    sec_dict = {0:2, 1:1, 2:2, 3:3, 4:2, 5:4, 6:2, 7:5}
    thir_dict = {0:3, 1:3, 2:1, 3:1, 4:2, 5:2, 6:4, 7:4, 8:5, 9:5}
    fir_value, sec_value, thir_value = 0, 0, 0
    
    for i in range(len(answers)):
        fir = i % 5
        sec = i % 8 
        thir = i % 10
        
        if answers[i] == fir_dict[fir]:
            fir_value += 1     
        if answers[i] == sec_dict[sec]:
            sec_value += 1
        if answers[i] == thir_dict[thir]:
            thir_value += 1
    max_value = max(fir_value, sec_value, thir_value)
    
    if max_value == fir_value:
        answer.append(1)
    if max_value == sec_value:
        answer.append(2)
    if max_value == thir_value:
        answer.append(3)
    
    return answer