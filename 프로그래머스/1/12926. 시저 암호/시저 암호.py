# 아스키코드 : ord() , chr() 
# ord('a') =97, z = 122


def solution(s, n):
    answer = ''
    for wr in s:
        if wr == ' ':
            answer += ' '
        elif ord(wr) <= 122 and ord(wr) >= 97:
            check = ord(wr)+n 
            if check > 122:
                answer += chr(check-26)
            else:
                answer += chr(check)
        elif ord(wr) <= 90 and ord(wr) >= 65:
            check = ord(wr) + n
            if check > 90:
                answer += chr(check-26)
            else:
                answer += chr(check)
                
    return answer