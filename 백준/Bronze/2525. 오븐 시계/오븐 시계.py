hour, minute = map(int, input().split())
time = int(input())

spend_time = minute + time
spend_time_hour = int(spend_time / 60)
spend_time_minute = spend_time % 60

if spend_time >= 60:
    hour = hour + spend_time_hour
    minute = spend_time_minute
    if hour >= 24:
        hour = hour - 24
    print(hour, minute)

else:
    minute = spend_time
    print(hour, minute)
    