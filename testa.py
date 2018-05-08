# _*_ coding:utf-8 _*_
__author__ = 'Xbc'


def intro():
    intros = filter(lambda x: True if x else False,
                    ['郭敬明', '大象', str(35)])
    print(type(intros))
    return ' / '.join(intros)

a = intro()
print(a)