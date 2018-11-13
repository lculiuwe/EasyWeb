from django.conf.urls import url
from cms import views

# url的匹配
urlpatterns = [
    # 首页
    url(r'^$', views.IndexView.as_view(), name='index'),
    # 文章详情页，()内的表示参数,等同于r'^article/(?P<pk>\d+)/$'，？P<pk>表示指定参数名为pk
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category_list, name='category'),
]
