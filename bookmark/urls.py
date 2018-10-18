from . import views
from django.urls import path

app_name = 'bookmark'
urlpatterns = [
    #/bookmark/
    path('', views.BookmarkModelView.as_view(), name='index'),
    #/bookmark/bookmark_list/
    path('bookmark_list/', views.BookmarkList.as_view(), name='bookmark_list'),
    #/bookmark/bookmark_list/99
    path('bookmark_list/<int:pk>', views.BookmarkDetail.as_view(), name='bookmark_detail'),
]