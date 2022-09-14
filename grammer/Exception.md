# <span style = "color : ">예외 처리</span>
## <span style = "color : orange">예외 처리 구문</span>
예외 처리할 문단을 try로 감싼다
```python
try:
    print("나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 /num2)))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err: # 모든 예외 처리
    print(err)
```
## <span style = "color : orange">예외 발생시키기</span>
raise를 이용해 발생시킨다
```python
try:
    print("나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    
    if num1 < 0 or num2 < 0:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError:
    print("음수를 입력하셨습니다.")
```
## <span style = "color : orange">사용자 정의 예외처리</span>
```python
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 나누기 전용 계산기 입니다.")
    num1 = int(input("한 자리 수를 입력하세요."))
    num2 = int(input("한 자리 수를 입력하세요."))
    
    if num1 >=10 or num2 >= 10:
        raise BigNumberError("입력 값 : {0} {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except BigNumberError as err:
    print("두 자리 숫자를 입력하셨습니다. 다시 입력하세요.")
    print(err)
```
## <span style = "color : orange">finally</span>
finally - 무조건 실행되는 문장 / error가 발생하고 프로그램이 꺼지는 상황을 방지해 완성도를 높힌다
```python
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 나누기 전용 계산기 입니다.")
    num1 = int(input("한 자리 수를 입력하세요."))
    num2 = int(input("한 자리 수를 입력하세요."))
    
    if num1 >=10 or num2 >= 10:
        raise BigNumberError("입력 값 : {0} {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except BigNumberError as err:
    print("두 자리 숫자를 입력하셨습니다. 다시 입력하세요.")
    print(err)
finally:
    print("이용해 주셔서 감사합니다.")
```