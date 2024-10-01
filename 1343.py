poly = input()

poly = poly.replace("XXXX", "AAAA")
poly = poly.replace("XX", "BB")

if 'X' in poly:
    print(-1)
    
else:
    print(poly)


##########

# poly = input().split('.')
# str = ''

# for i in poly:
#     if len(i) % 2 == 1:
#         print(-1)
#         break
    
#     while len(i) >= 4:
#         str += 'AAAA'
#         i = i[4:]
#     if len(i) == 2:
#         str += 'BB'
#         i = i[2:]

#     str+='.'

# else:
#     print(str[:-1])