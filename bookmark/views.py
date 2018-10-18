from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from bookmark.models import Bookmark

# Create your views here.
#--TemplateView
class BookmarkModelView(TemplateView):
    template_name = 'bookmark/index.html'

    def get_context_data(self, **kwargs):   #get_context_data method 정의시, super() method 반드시 호출!
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Bookmark']
        return context


#--ListView
class BookmarkLV(ListView):
    model = Bookmark

#--DetailView
class BookmarkDV(DetailView):
    model = Bookmark