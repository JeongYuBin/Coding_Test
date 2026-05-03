# https://school.programmers.co.kr/learn/courses/30/lessons/120808'
# 최대 공약수 구하기 
# 나눗셈 / : 실수 , // : 정수

def solution(numer1, denom1, numer2, denom2):
    numer = numer1*denom2 + numer2*denom1
    denom = denom1*denom2
    
    # 최대공약수 구하기(유클리드 호제법)
    # 반복이 끝나면 a가 최대 공약수
    # numer = 분자 , denom = 분모
    a, b = numer, denom
    while b:
        a, b = b, a % b
    gcd = a 
    numer //= gcd
    denom //= gcd
    answer = [numer, denom]
    
    return answer