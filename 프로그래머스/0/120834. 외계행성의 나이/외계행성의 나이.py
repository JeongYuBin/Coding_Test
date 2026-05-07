def solution(age):
    answer = ''  # a 아스키 코드 : 97  # 숫자 -> 아스키 chr()
    a = age % 1000 % 100 % 10  # 1의 자리 
    b = age % 1000 % 100 // 10 # 10의 자리
    c = age % 1000 // 100      # 100의 자리
    d = age // 1000
    if age >= 1000:
        answer += chr(d+97)
    if age >= 100:
        answer += chr(c+97)
    if age >= 10:
        answer += chr(b+97)
    answer += chr(a+97)
    return answer