#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from mt.models import Movie
from django.http import HttpResponse


def testORM(request):
    result = Movie.objects.all()
    name = ''
    for x in result:
        name = x.name
        break
    return HttpResponse(name)

def changeData(request):
    # 插入
    m1 = Movie(name='狂暴巨兽', show_time='2018-4', type='科幻')
    m1.save()
    m2 = Movie(name='托尔斯泰', show_time='2018-4', type='科幻')
    m2.save()
    m3 = Movie(name='烦烦烦', show_time='2018-5', type='科幻')
    m3.save()

    # 修改
    # m = Movie.objects.get(name='托尔斯泰')
    # m.name = '太空堡垒'
    # m.save()

    # 删除
    # m = Movie.objects.get(name='烦烦烦')
    # m.delete()

    # 删除所有
    # Movie.objects.all().delete()
    return HttpResponse('数据修改成功')

def filter(request):
    # 过滤所有数据
    # all = Movie.objects.all()
    # result = ""
    # for d in all:
    #     result = result + d.name + ','

    # 过滤特定对象
    # ok = Movie.objects.filter(name='托尔斯泰', type='科幻')

    # 包含字段
    ok = Movie.objects.filter(name__icontains='泰', type='科幻')
    return HttpResponse(ok[0].type)

def oneObject(request):
    # filter return QuerySet
    # get 返回一个对象(模型对象)
    try:
        m = Movie.objects.get(name='托尔斯泰1')
        print(type(m))
        # class 'mt.models.Movie'>

        print(type(Movie.objects.filter(name='托尔斯泰')))
        # class 'django.db.models.query.QuerySet'>
        # 如果没有查询到任何数据会抛出DoesNotExist异常,或多余一条记录会抛出MultiObjectsReturned异常,
    except Movie.DoesNotExist:
        return HttpResponse('没有查到任何数据')
    except Movie.MultipleObjectsReturned:
        return HttpResponse('查询结果多余一条记录')
    return HttpResponse('查询成功')

def dataOrder(requets):
    # 默认为升序, 加'-'为降序
    # dataSet = Movie.objects.order_by('name') # 正序
    dataSet = Movie.objects.order_by('-name') # 倒序
    # dataSet = Movie.objects.order_by('-show_time', type)  # 复合排序
    result = ''
    for d in dataSet:
        result = result + d.name + ','
    return HttpResponse(result)

# 连锁查询
def multiQuery(request):
    dataSet = Movie.objects.filter(type__icontains='科幻').order_by('name')
    result = ''
    for d in dataSet:
        result = result + d.name + ','
    return HttpResponse(result)

# 限制返回的数量(返回查询结果集的子集)
"""
select * from table1 where name like '%abc' limit 1,10  # 返回从第2记录开始的10条记录,2-11条记录
"""

def limitData(request):
    # 不支持负数索引
    dataSet = Movie.objects.order_by('name')[1:3] # limit 1,2
    result = ''
    for d in dataSet:
        result = result + d.name + ','
    return HttpResponse(result)

"""
指定更新列
    m = Movie.objects.get(name='托尔斯泰')
    m.name = '太空堡垒'
    m.save()
    update mt_movie set name='太空堡垒',type='科幻',show_time='2018-4' where name='托尔斯泰'
"""
def update(request):
    # update mt_movie set name='太空堡垒' where name='托尔斯泰'
    Movie.objects.filter(name='托尔斯泰').update(name='西虹市首富')
    return HttpResponse('更新成功')