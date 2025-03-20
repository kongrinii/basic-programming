choice1 = input()
choice2 = input()

if choice1 not in ["가위", "바위", "보"] or choice2 not in ["가위", "바위", "보"]:
    print("올바른 입력을 하세요")

elif choice1 == choice2:
    print("무승부")
    
elif (choice1 == "가위" and choice2 == "보") or \
     (choice1 == "바위" and choice2 == "가위") or \
     (choice1 == "보" and choice2 == "바위"):
    print("승리")
else:
    print("패배")