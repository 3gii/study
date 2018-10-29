import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer

# 常规实现restful api
# class BookListView(View):
#     """查询所有图书，增加图书"""
#
#     def get(self, request):
#         """
#         查询所有图书
#         路由：GET /books/
#         :param request:
#         :return:
#         """
#         queryset = BookInfo.objects.all()
#         book_list = []
#         for book in queryset:
#             book_list.append({
#                 'id': book.id,
#                 'btitle': book.btitle,
#                 'bpub_date': book.bpub_date,
#                 'bread': book.bread,
#                 'bcomment': book.bcomment,
#                 'image': book.image.url if book.image else ''
#             })
#         return JsonResponse(book_list, safe=False)
#
#     def post(self, request):
#         """
#         新增图书
#         路由： POST /books/
#         :param request:
#         :return:
#         """
#         json_bytes = request.body
#         json_str = json_bytes.decode()
#         book_dict = json.loads(json_str)
#
#         # 校验
#         book = BookInfo.objects.create(
#             btitle = book_dict.get('btitle'),
#             bpub_date = book_dict.get('bpub_date')
#         )
#
#         return JsonResponse({
#             'id': book.id,
#             'btitle': book.btitle,
#             'bpub_date': book.bpub_date,
#             'bread': book.bread,
#             'bcomment': book.bcomment,
#             'image':book.image.url if book.image else ''
#         }, status=201)
#
#
# class BookDetailView(View):
#     """图书详情"""
#
#     def get(self, request, pk):
#         """
#         获取单个图书信息
#         路由：GET /books/<pk>/
#         :param request:
#         :param pk:
#         :return:
#         """
#         try:
#             book = BookInfo.objects.get(pk=pk)
#         except BookInfo.DoesNotExist:
#             return HttpResponse(status=404)
#
#         return JsonResponse({
#             'id': book.id,
#             'btitle': book.btitle,
#             'bpub_date': book.bpub_date,
#             'bread': book.bread,
#             'bcomment': book.bcomment,
#             'image': book.image.url if book.image else ''
#         })
#
#     def put(self, request, pk):
#         """
#         修改图书信息
#         路由：PUT /books/<pk>/
#         :param request:
#         :param pk:
#         :return:
#         """
#         try:
#             book = BookInfo.objects.get(pk=pk)
#         except BookInfo.DoesNotExist:
#             return HttpResponse(status=404)
#
#         json_bytes = request.body
#         json_str = json_bytes.decode()
#         book_dict = json.loads(json_str)
#
#         # 参数校验
#         book.btitle = book_dict.get('btitle')
#         book.bpub_date = book_dict.get('bpub_date')
#         book.save()
#         return JsonResponse({
#             'id': book.id,
#             'btitle': book.btitle,
#             'bpub_date': book.bpub_date,
#             'bread': book.bread,
#             'bcomment': book.bcomment,
#             'image': book.image.url if book.image else ''
#         })
#
#
#     def delete(self, request, pk):
#
#         try:
#             book = BookInfo.objects.get(pk=pk)
#         except BookInfo.DoesNotExist:
#             return HttpResponse(status=404)
#
#         book.delete()
#         return HttpResponse(status=204)
#
#
# class BookInfoViewSet(ModelViewSet):
#
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#


# 使用DRF  APIView
# class BookListView(APIView):
#
#     def get(self, request):
#         books = BookInfo.objects.all()
#         serializer = BookInfoSerializer(books, many=True)
#         return Response(serializer.data)



# class BookDetailView(GenericAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#     def get(self, request, pk):
#         book = self.get_object()
#         serializer = self.get_serializer(book)
#         return Response(serializer.data)

class BookListView(GenericAPIView, ListModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    def get(self, request):
        return self.list(request)

class BookDetailView(GenericAPIView, RetrieveModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    def get(self, request, pk):

        return self.retrieve(request)

class BookCreateView(GenericAPIView, CreateModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    def post(self, request):

        return self.create(request)


class BookListViewSet(ViewSet):
    def list(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)

class MyPermission(BasePermission):

    def has_permission(self, request, view):
        """判断对使用此权限类的视图是否有访问权限"""

        # 任何用户对使用此权限类的视图都没有访问权限
        return True


    def has_object_permission(self, request, view, obj):
        """判断对使用此权限类视图某个数据对象是否有访问权限"""
        if obj.id in (1, 3):
            return True
        return False

class BookInfoViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    # 指定当前视图所使用的认证类
    authentication_classes = [SessionAuthentication]
    # 指定当前视图所使用的权限控制类
    # permission_classes = [IsAuthenticated]
    #使用自定义权限控制类
    permission_classes = [MyPermission]

    def latest(self, request):
        """
        返回最新的图书信息
        """
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    def read(self, request, pk):
        """
        修改图书的阅读量数据
        """
        book = self.get_object()
        book.bread = request.data.get('read')
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)
