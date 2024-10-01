num = [int(input()) for i in range (int(input()))]

num.sort()
count = 0

for i in range (len(num)) : 
    count += abs(num[i] - (i+1))

print(count)