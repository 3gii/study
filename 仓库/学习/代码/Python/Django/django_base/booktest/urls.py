from django.conf.urls import url
from booktest import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # url(r'^books/$', views.BookListView.as_view()),
    # url(r'^books/$', views.BookCreateView.as_view()),
    # url(r'^books/$', views.BookListViewSet.as_view({'get': 'book_list'})),
    url(r'^books/$', views.BookInfoViewSet.as_view({'get': 'list'})),
    url(r'^books/latest$', views.BookInfoViewSet.as_view({'get': 'latest'})),
    url(r'^books/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({'get': 'retrieve'})),
    url(r'^books/(?P<pk>\d+)/read', views.BookInfoViewSet.as_view({'put': 'read'})),
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view())
]


# router = DefaultRouter()
# router.register('books', views.BookInfoViewSet, base_name='books')
# urlpatterns += router.urls