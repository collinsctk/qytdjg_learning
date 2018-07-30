#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

# 通用视图类
# 简单的通用视图类
from django.http import HttpResponse
from django.views.generic import View

class MyView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('Hello World')

# 可以向模板中传递变量值的通用类
from django.views.generic.base import TemplateView
class HomePageView(TemplateView):
    template_name = "product.html"
    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        context['mobile_product1'] = 'iPhone'
        context['mobile_product2'] = 'Android'
        return context

# 列表视图(ListVeiw)
from django.views.generic import ListView
from mt.models import Movie

class MovieView(ListView):
    model = Movie
    template_name = 'movie_view.html'
    context_object_name = 'movies'


class QueryMovieView(ListView):
    model = Movie
    template_name = 'movie_view.html'
    context_object_name = 'movies'
    def get_queryset(self):
        return super(QueryMovieView,self).get_queryset().filter(type='科幻')

class ParamQueryMovieView(ListView):
    model = Movie
    template_name = 'movie_view.html'
    context_object_name = 'movies'
    def get_queryset(self):
        name = self.request.GET.get('name')
        return super(ParamQueryMovieView,self).get_queryset().filter(name=name)

# 细节视图(DetailView)
from django.views.generic import DetailView
# http://10.1.1.80:8000/movie_detail/12/
class MovieDetailView(DetailView):
    queryset = Movie.objects.all()
    template_name = 'movie_detail.html'
    context_object_name = 'movie'
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return obj


if __name__ == "__main__":
    pass