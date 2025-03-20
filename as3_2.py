#미세먼지 상태 판별기 프로그램
#현재 미세먼지 농도 A를 사용자로부터 입력받은 다음, 현재 미세먼지 상태를 '좋음', '보통', '나쁨', '매우 나쁨' 중 하나로 판별해 출력하는 프로그램을 작성하시오.
#2114885 오경린

density = int(input())

if 0 <= density <= 15:
    print("좋음")
elif 16 <= density <= 35:
    print("보통")
elif 36 <= density <= 75:
    print("나쁨")
else:
    print("매우 나쁨")