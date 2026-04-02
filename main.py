# 파일이름 :60252667 김예성 1차과제
# 작 성 자 :김예성

#1. 사용자 입력 받기
name=input("이름을 입력하세요: ")
money=int(input("투자금을 입력하세요 (원): "))
rate=float(input("수익률을 입력하세요 (%): "))

#2. 수익 계산
profit = money * rate / 100
total = money + profit

#3. 결과 출력
print("\n=====투자결과=====")
print(f"이름: {name}")
print(f"투자금: {money}원")
print(f"수익률: {rate}%")
print(f"예상 수익: {int(profit)}원")
print(f"총 금액:{int(total)}원")

