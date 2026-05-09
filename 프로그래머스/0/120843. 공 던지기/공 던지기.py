def solution(numbers, k):
    answer = 0
    if len(numbers) % 2 == 0:
        q = k % (len(numbers) // 2) # 위치
        if q == 0:
            q = len(numbers) // 2
        answer = numbers[2*q - 2]
    else:
        q = k % len(numbers)
        if q == 0:
            q = len(numbers)
        answer = numbers[(2*q - 2) % len(numbers)]
        
    return answer