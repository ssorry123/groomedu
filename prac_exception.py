''' 사용자 정의 에러 처리 '''
class BigNumberError(Exception):
    #pass
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

''' 예외 처리 '''
print("나누기 전용 계산기")
try:
    nums = list()
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format( nums[0], nums[1], nums[2]))
except ValueError as err:
    print("에러! 잘못된 값을 입력하였습니다.")
    print(err)
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")

''' 예외 발생 '''
print("한 자리 숫자 나누기 전용 계산기")
try:
    num1 = int(input("첫 번째 숫자 입력 : "))
    num2 = int(input("두 번째 숫자 입력 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력 값에 한 자리 수만 입력하세요")
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except BigNumberError as err:
    print(err)

