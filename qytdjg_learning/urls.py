"""qytdjg_learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import DB,qytindex,Form,CommonViewClass,MyTemplate
from django.views.generic.base import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('simpletemplate/', MyTemplate.simpleTemplate),
    path('multicontext/', MyTemplate.multiContext),
    path('loadtemplatefile/', MyTemplate.loadTemplateFile),
    path('loadtemplatefile1/', MyTemplate.loadTemplateFile1),
    path('loadtemplatefile2/', MyTemplate.loadTemplateFile2),
    path('ifelsetemplate/', MyTemplate.ifelseTempalte),
    path('multicondition/', MyTemplate.multicondition),
    path('equalvar/', MyTemplate.equalVar),
    path('forlist/', MyTemplate.forList),
    path('filter/', MyTemplate.temp_filter),
    path('includetemp/', MyTemplate.include_temp),
    path('sub1/', MyTemplate.sub1),
    path('sub2/', MyTemplate.sub2),
    path('testdb/', DB.testORM),
    path('changeData/', DB.changeData),
    path('filter/', DB.filter),
    path('oneobject/', DB.oneObject),
    path('dataorder/', DB.dataOrder),
    path('multiquery/', DB.multiQuery),
    path('limitdata/', DB.limitData),
    path('update/', DB.update),
    path('requestinfo/', Form.requestInfo),
    path('searchform/', Form.searchForm),
    path('search/', Form.search),
    path('searchverify/', Form.searchVerify),
    path('searchverifyad/', Form.searchVerifyad),
    path('contact/', Form.contact),
    path('myview/', CommonViewClass.MyView.as_view()),
    path('homepage/', CommonViewClass.HomePageView.as_view()),
    path('ciscohome/', RedirectView.as_view(url='http://www.cisco.com')),
    path('movieview/', CommonViewClass.MovieView.as_view()),
    path('movieviewquery/', CommonViewClass.QueryMovieView.as_view()),
    path('movie_detail/<int:pk>/', CommonViewClass.MovieDetailView.as_view()),
    path('', qytindex.index),
]
