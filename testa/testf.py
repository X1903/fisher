# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from werkzeug.local import LocalStack

s = LocalStack()
s.push(1)   # 添加
print(s.top)  # 取
print(s.top)  # 取
print(s.pop()) # 删除
print(s.top)   # 取

# 1
# 1
# 1
# None

s.push(1)
print(s.top)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

# 1
# 2
# 2
# 2
# 1