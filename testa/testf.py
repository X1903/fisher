# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from werkzeug.local import LocalStack

s = LocalStack()
# push  pop  top

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
# 栈 后进先出
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

# s[7] 栈  序列(列表)
# 数据结构  限制了某些能力

# 1
# 2
# 2
# 2
# 1