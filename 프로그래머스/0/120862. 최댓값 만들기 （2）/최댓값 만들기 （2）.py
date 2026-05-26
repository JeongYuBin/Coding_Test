def solution(numbers):
    answer = 0
    gob = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            gob.append(numbers[i]*numbers[j])
            
    answer = max(gob)
    return answer