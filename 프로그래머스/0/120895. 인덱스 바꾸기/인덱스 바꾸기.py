def solution(my_string, num1, num2):
    answer = ''
    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]
    
    return ''.join(s) #문자열들을 하나로 이어붙이는 함수