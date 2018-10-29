#### 环境安装

1. 安装DRF
   `pip insatll djangorestframework`

2. 添加rest_framework

   ```python
   INSTALLED_APPS = [
   	...
       'rest_framework',
   ]
   ```

####创建序列化器

> 在app目录下新建serializers.py

```python
# 序列化器
from rest_framework import serializers

from booktest.models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookInfo
        fields = '__all__'
```

#### 编写视图

```python
class BookInfoViewSet(ModelViewSet):

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
```

#### 定义路由

```python
from django.conf.urls import url
from booktest import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # url(r'^books/$', views.BookListView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view())
]


router = DefaultRouter()
router.register('books', views.BookInfoViewSet, base_name='books')
urlpatterns += router.urls
```

