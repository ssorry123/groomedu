# 내장 함수 : import 하지 않아도 사용 가능

# input
lang = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(lang))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random
print(dir())

print(dir(random))

lst = [1, 2, 3]
print(dir(lst))

name = "asdasf"
print(dir(name))

''' 문서 '''
# list of python builtins