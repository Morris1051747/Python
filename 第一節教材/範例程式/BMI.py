height = 181 #身高
weight = 65  #體重

"""
BMI = 體重(公斤) / 身高平方(公尺)
"""

height = 181/100          # height = 1.81
height = height * height  # height = 1.81 x 1.81

BMI = weight / height

if BMI <= 18.4:
    print('你太瘦了')
elif BMI<=23.9:
    print('你好正常')
elif BMI<=27.9:
    print('你胖胖的')
elif BMI>=28:
    print('你太大隻了')




