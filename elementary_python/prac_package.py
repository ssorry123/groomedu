'''test1'''
# 패키지는 모듈들의 모임
# 클래스나 함수는 직접 바로 import를 할 수 없다

# 클래스 or 함수 << 모듈 << 패키지

import travel.thailand  # 패키지의 모듈 import
from travel import thailand # 패키지의 모듈 import
from travel.vietnam import VietnamPackage # 패키지의 모듈의 클래스 import

trip_to0 = travel.thailand.ThailandPackage()
trip_to0.detail()

trip_to1 = thailand.ThailandPackage()
trip_to1.detail()

trip_to2 = VietnamPackage()
trip_to2.detail()

'''test2'''
#from random import *
# 개발자가 *의 범위를 정의해주어야 한다. __init__.py

from travel import *
trip_to3 = vietnam.VietnamPackage()     # 정의 해서 가능
#trip_to4 = thailand.ThailandPackage()   # 정의 안해서 불가능
trip_to3.detail()

'''test3'''
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))