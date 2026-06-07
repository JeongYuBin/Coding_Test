def solution(numlist, n):
    answer = []
    for i in numlist:
        answer.append([abs(i - n), -i, i])
    answer.sort()
    return  [x[2] for x in answer] 