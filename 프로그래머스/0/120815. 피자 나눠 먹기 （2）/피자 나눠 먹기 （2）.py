def solution(n):
    i = 1
    while True:
        # n * i의 배수가 6의 배수랑 같아지는 경우 stop
        if (6 * i) % n == 0 :
            return i
        i += 1
        