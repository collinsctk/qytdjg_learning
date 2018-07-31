#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render

# 表单
# 获取客户端请求的相关信息


def requestInfo(request):
    result = 'path: %s ' % request.path
    result = result + '<br>host: %s ' % request.get_host()
    result = result + '<br>full_path %s ' % request.get_full_path()
    result = result + '<br>port: %s ' % request.get_port()
    result = result + '<br>https: %s ' % request.is_secure()
    # request.META: Python字典, 包含所有HTTP请求头
    try:
        result = result + '<br>Accept: %s ' % request.META['HTTP_ACCEPT']
    except KeyError:
        result = result + '<br>HTTP请求头获取异常'
    # 下面是展示META内部的键值
    # values = request.META.items()
    # sorted(values)
    # html = []
    # for key,value in values:
    #     html.append('<tr><td>%s</td><td>%s</td></tr>' % (key,value))
    #
    # return HttpResponse('<table>%s</table>' % '\n'.join(html))
    return HttpResponse(result)


# 处理表单(Form)提交的数据
def searchForm(request):
    return render_to_response('search_form.html')


# def search(request):
#     if 'name' in request.GET:
#         message = 'You searched for:%s' % request.GET['name']
#     else:
#         message = 'You submmited an empty form.'
#     return HttpResponse(message)

# 从数据库查询数据
from mt.models import Movie

# def search(request):
#     if 'name' in request.GET:
#         name = request.GET['name']
#         movies = Movie.objects.filter(type__icontains=name)
#         return render_to_response('search_results.html', {'movies':movies, 'query':name})
#     else:
#         return HttpResponse('Pls submit a search term.')

# 改进表单
def search(request):
    if 'name' in request.GET:
        name = request.GET['name']
        movies = Movie.objects.filter(type__icontains=name)
        return render_to_response('search_form_ext.html', {'movies':movies, 'query':name})
    else:
        return render_to_response('search_form_ext.html', {'error':True})

# 简单的表单校验
def searchVerify1(request):
    error = False
    if 'name' in request.GET:
        name = request.GET['name']
        # name必须有值
        if not name:
            error = True
        elif len(name) > 10:
            error = True
        else:
            movies = Movie.objects.filter(type__icontains=name)
            return render_to_response('search_form_ext_verify.html', {'movies':movies, 'query':name})

    return render_to_response('search_form_ext_verify.html', {'error':True})

def searchVerify(request):
    errors = []
    if 'name' in request.GET:
        name = request.GET['name']
        # name必须有值
        if not name:
            errors.append('请输入电影类型名')
        elif len(name) > 10:
            errors.append('电影类型名长度不能大于10')
        else:
            movies = Movie.objects.filter(type__icontains=name)
            return render_to_response('search_form_ext_verify2.html', {'movies':movies, 'query':name})

    return render_to_response('search_form_ext_verify2.html', {'errors':errors})


# 复杂的表单校验
def searchVerifyad(request):
    errors = []
    if 'name' in request.GET:
        name = request.GET['name']
        value1 = request.GET['value1']
        value2 = request.GET['value2']
        # name必须有值
        if not name:
            errors.append('请输入电影类型名')
        if not value1:
            errors.append('必须提供value1')
        if not value2:
            errors.append('必须提供value2')


        if not errors:
            movies = Movie.objects.filter(type__icontains=name)
            return render_to_response('search_form_ext_verifad.html', {'movies':movies, 'query':name})

    return render_to_response('search_form_ext_verifyad.html', {'errors':errors})

# 编写Form类
# django.forms.Form

# 在视图中使用Form对象
from mt.forms import MyForm
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# from django.views.decorators.csrf import csrf_protect
# from django.middleware.csrf import get_token
# @csrf_protect


# def contact(request):
#     # print(get_token(request))
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             print('完成与业务相关的工作')
#             return HttpResponse('OK')
#         else:
#             return render_to_response('my_form.html',{'form':form, 'csrf_token':get_token(request)})
#     else:
#         form = MyForm(initial={'name':'秦柯', 'email':'collinsctk@qytang.com', 'message':'没有信息'}) # 初始值
#         return render_to_response('my_form.html',{'form':form, 'csrf_token':get_token(request)})

# 处理CSRF问题
def contact(request):
    # print(get_token(request))
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print('完成与业务相关的工作')
            return HttpResponse('OK')
        else:
            return render(request,'my_form.html',{'form':form})
    else:
        form = MyForm(initial={'name':'秦柯', 'email':'collinsctk@qytang.com', 'message':'没有信息'}) # 初始值
        return render(request,'my_form.html',{'form':form})

if __name__ == "__main__":
    pass