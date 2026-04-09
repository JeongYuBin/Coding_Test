a, b, c = map(int, input().split())

if a==b==c:
    print(10000 + a*1000)
elif a==b!=c or a!=b==c or a==c!=b :
    if a==b!=c:
        print(1000 + a*100)
    elif a!=b==c:
        print(1000 + b*100)
    else :
        print(1000 + c*100)
else :
    result = sorted([a,b,c], reverse=True)
    print(result[0]*100)