total_price = int(input())
price = 0
N = int(input())
for i in range(N):
    num1, num2 = map(int, input().split())
    price += num1 * num2

if total_price == price :
    print('Yes')
else:
    print('No')