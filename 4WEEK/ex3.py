# 함수가 장의가 되어 있는 가?
# 함수를 담은 라이브러리를 import 했는가?
def sum_int(a, b): # (:) 콜론 필수
    return a+b     # 들여쓰기 블록 정의 
# return = 함수 종료

num1 = 10
num2 = 20

result = sum_int(num1, num2)
print(f'{num1} + {num2} = {result}')

print("--------------------------------------------------------")

def int(a, b):
    return a * b

num1 = 9
num2 = 11

mult = int(num1, num2)
print(f'{num1} * {num2} = {mult}')