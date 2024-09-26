def sumfunc(n):
    return sum (range(1, n+1))

num = int(input("정수를 입력하세요."))

if num <= 1:
    print("잘못 입력하셨습니다.")
else:
    print(f'1부터 {num}까지의 합 : {sumfunc(num)}')

