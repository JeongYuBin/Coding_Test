def solution(lottos, win_nums):
    correct = 0
    wildcard = 0
    for lo in lottos:
        if lo == 0:
            wildcard += 1
        elif lo in win_nums:
            correct += 1        
    
    maxvalue = correct + wildcard
    diction = {6:1, 5:2, 4:3, 3:4, 2:5}
    
    if maxvalue < 2:
        return [6, 6]
    
    maxvalue = diction[maxvalue]
    
    if correct > 1:
        correct = diction[correct]
    else:
        correct = 6
    return [maxvalue, correct]