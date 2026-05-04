def solution(slice, n):
    i = 1
    while True:
        if (slice * i) // n > 0 : 
            return i 
        i += 1