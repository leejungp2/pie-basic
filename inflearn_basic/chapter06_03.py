# Chapter 06_03
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할된 개별적인 모듈로 구성
# 상대경로 : .. 부모 디렉토리, . 현재 디렉토 -> 모듈 내부에서만 사용
# __init__.py : 파이썬 3.3부터는 없어도 패키지로 인식, but 하위호환을 위해 작성

# 예제 1

import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제2
from sub.sub1 import module
from sub.sub2 import module as m2 # alias

module1.mod1_test()
module1.mod1_test2()

print()
print()
print()

# 예제3
from sub.sub1 import * # 모듈 전체를 가져옴
module1.mod1_test()
