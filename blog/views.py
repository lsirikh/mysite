from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.dates import MonthArchiveView, DayArchiveView, TodayArchiveView

from blog.models import Post

# Create your views here.

#--TemplateView
class PostModelView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):   #get_context_data method 정의시, super() method 반드시 호출!
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Post']
        return context

#--ListView
class PostList(ListView):
    model = Post

#--DetailView
class PostDetail(DetailView):
    model = Post


#--ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView):
    model =Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model =Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model =Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView):
    model =Post
    date_field = 'modify_date'