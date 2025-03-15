#2114885 IT공학과 오경린
#과제 2_3번
#두 점을 입력받아 유클리드 거리르 계산하는 프로그램
#0315 
import math

x1,y1 = map(float, input("Enter x1 and y1: ").split())
x2,y2 = map(float,input("Enter x2 and y2: ").split())

d = math.sqrt((x2-x1) **2 + (y2-y1)**2)
#math.sqrt 이용하여 제곱근 계산
print(f"The distance of the two points is {d}")