def solution(common):
    answer = 0
    check = 0
    double_check = 0 
    first = 0
    second = 0 

    for i in common:
        if first == 0:
            first = i
        elif check == 0:
            check = i - first
            second = i
        elif double_check == 0:
            double_check = i - second
    if check == double_check: 
        answer = common[-1]+check
    else:
        gob = double_check // check
        answer = common[-1]*gob
            
    return answer