Hour, Minute = map(int, input().split())

# 45min 빼기

if Minute >= 45 :
    Minute -= 45
    print(Hour, Minute)

else:
    Minute += 15
    Hour -= 1
    if Hour < 0 :
        Hour = 23
    print(Hour, Minute)
