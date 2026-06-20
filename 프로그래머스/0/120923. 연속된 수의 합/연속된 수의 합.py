def solution(num, total):
    answer = []
    start = 0
    
    # total = start * num + (num(num-1) / 2)
    start = (total - num * (num-1) // 2) // num
    
    for i in range(start, start+num):
        answer.append(i)
    
    return answer