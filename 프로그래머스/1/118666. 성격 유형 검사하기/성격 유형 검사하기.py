def solution(survey, choices):
    answer = ''
    diction = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    check = ''
    
    # 해당 나오는 값에 점수만큼 알파벳 추가해서 check.count('R') 한 뒤에 대소 비교하면 될듯?
    for i in range(len(survey)):
        if choices[i] <=3:
            for _ in range(diction[choices[i]]):
                check += survey[i][0]
        elif choices[i] >=5:
            for _ in range(diction[choices[i]]):
                check += survey[i][1]
                
    # RT 비교(R이 T보다 빠름)
    R = check.count('R')
    T = check.count('T')
    if R >= T:
        answer += 'R'
    else:
        answer += 'T'
    
    # CF 비교(C가 F보다 빠름)
    C = check.count('C')
    F = check.count('F')
    if C >= F:
        answer += 'C'
    else:
        answer += 'F'
    
    # JM 비교(J가 M보다 빠름)
    J = check.count('J')
    M = check.count('M')
    if J >= M:
        answer += 'J'
    else:
        answer += 'M'
    
    # AN 비교(A가 N보다 빠름)
    A = check.count('A')
    N = check.count('N')
    if A >= N:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer