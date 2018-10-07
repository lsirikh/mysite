"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #path('', views.index, name = 'index'),
    #path('<int:question_id>/', views.detail, name = 'detail'),
    #path('<int:question_id>/results/', views.results, name = 'results'),
    #path('<int:question_id>/vote/', views.vote, name = 'vote'),

    #/polls/
    path('', views.IndexView.as_view(), name='index'),

    #/polls/99/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    #/polls/99/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    #/polls/99/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

]


