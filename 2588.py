a = int(input())  # 472
b = int(input())  # 385
 
b_first = b%100%10
b_second = int(b%100/10)  # 8.5
b_third = int(b/100)

third_answer = b_first * a
forth_answer = b_second * a
fifth_answer = b_third * a
sixth_answer = a * b

print(third_answer)
print(forth_answer)
print(fifth_answer)
print(sixth_answer)