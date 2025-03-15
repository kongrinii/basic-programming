#2114885 IT공학과 오경린
#Assignment 2-1 덧셈 프로그램

A,B = map(int, input().split())
#split를 사용하면 공백 기준으로 문자열을 리스트로 반환
#정수로 변환해야 연산 가능
#map(int) 이용

if 0<A<10 and 0 < B < 10:
    print(A+B)

else: 
    print("A 와 B 는 1 이상 9 이하")
