def solution(phone_number):
    answer = ''
    value = len(phone_number[:-4])
    answer += '*'*value + phone_number[-4:]
    
    return answer