def solution(n):
    answer = 0
    count = 0 
    while count < n:
        answer += 1
        if '3' in str(answer) :
            continue
        elif answer % 3 == 0:
            continue
        count += 1
    return answer
