def solution(n):
    prime = [True] * (n + 1)

    prime[0] = False
    prime[1] = False

    for i in range(2, n + 1):
        if prime[i]:
            for k in range(i * 2, n + 1, i):
                prime[k] = False

    return prime.count(True)