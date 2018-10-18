from . import views
from django.urls import path, re_path


app_name='blog'
urlpatterns = [
    # /blog/
    path('', views.PostModelView.as_view(), name='index'),
    # /blog/post
    path('post/', views.PostList.as_view(), name='post_list'),
    # /blog/post/django-examle/
    #re_path(r'^post/(?P<slug>[-\W]+)/$', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),

    #/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    #/2012/
    re_path(r'^(?P<year>\d{4})/$', views.PostYAV.as_view(), name='post_year_archive'),
    #/2012/nov/
    re_path(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', views.PostMAV.as_view(), name='post_month_archive'),
    #/2012/nov/10/
    re_path(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', views.PostDAV.as_view(), name='post_day_archive'),
    #/today/
    re_path('today/', views.PostTAV.as_view(), name='post_today_archive'),
]