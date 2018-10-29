from django.db.models import Q
from django.test import TestCase

# Create your tests here.

# 设置Django运行所依赖的环境变量
import os
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_base.settings')

# 初始化
import django
django.setup()

from booktest.models import BookInfo, HeroInfo, User, Student, StuInfo, NewsInfo, TypeInfo, AreaInfo
from booktest.serializers import BookInfoSerializer, HeroInfoSerializer
class Displayer():
    def display(self, message):
        print(message)


# class Logger():
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         super().display(message)
#         self.log(message)
#
#
# class MySubClass(Logger, Displayer):
#     def log(self, message):
#         super().log(message, filename='subclasslog.txt')
#
#
# subclass = MySubClass()
# print(MySubClass.mro())
# subclass.display("This string will be shown and logged in subclasslog.txt")

# 序列化使用
if __name__ == '__main__':
    # book = BookInfo.objects.get(id=2)
    # serializer = BookInfoSerializer(book)
    # book = serializer.data
    # print(book)

    # hbook = HeroInfoSerializer(book)
    # print(hbook)

    # data = {'btitle': 'python'}
    # serializer = BookInfoSerializer(data=data)
    # v = serializer.is_valid()
    # # print(v)
    # print(type(serializer))
    # print(serializer.data)
    #
    # print(serializer.validated_data)


    # s = serializer.errors
    # print(s)


    # data = {'btitle': '封神演义'}
    # serializer = BookInfoSerializer(data=data)
    # valid = serializer.is_valid()  # True
    # s = serializer.save()  # <BookInfo: 封神演义>
    #
    #
    #
    # book = BookInfo.objects.get(id=2)
    # data = {'btitle': '倚天剑'}
    # serializer = BookInfoSerializer(book, data=data)
    # v = serializer.is_valid()  # True
    # s = serializer.save()  # <BookInfo: 倚天剑>
    # b = book.btitle  # '倚天剑'
    pass
from collections import OrderedDict
class A(dict):

    def __init__(self, *args, **kwargs):
        super(A, self).__init__(*args, **kwargs)

a = A()
a = {
    'name': 'zhangsan'
}
print(a)