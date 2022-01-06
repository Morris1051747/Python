import math

"""
Ax^2 + Bx + C = 0
"""

A = 1
B = 3
C = -10

"""

2x^2 + 3x + 1 = 0

算出 b^2 - 4ac 的值
若 值 > 0，則 x = (-b 加減 根號 b^2 - 4ac) / 2a
若 值 = 0，則 x = -b / 2a（重根）
若 值 < 0，則 無解
"""

temp = B*B - 4*A*C
if temp < 0:
    print('無解啦')
elif temp ==0:
    X1 = -B / ( 2 * A )
    X2 = -B / ( 2 * A )
    print(X1)
    print(X2)
else:
    X1 = ( -B + math.sqrt(temp) ) / ( 2 * A )
    X2 = ( -B - math.sqrt(temp) ) / ( 2 * A )
    print(X1)
    print(X2)




