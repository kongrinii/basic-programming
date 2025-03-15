#2114885 IT공학과 오경린
#정수를 입력받아 자릿수의 합을 출력하는 프로그램
A = int(input("Enter a digit between 0 and 999: "))

digit_sum = 0
for digit in str(A):
    digit_sum += int(digit)


print(f"The sum of digits is {digit_sum}")
