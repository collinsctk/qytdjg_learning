#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

# 模板

# 静态和动态内容,动态内容就是模板变量,在将模板发送给客户端之前,需要将动态部分替换成相应的值
# 在Shell中使用Django模板,不应该直接使用Python REPL
# 要使用Python manage.py shell命令进入Django Shell
#
# from django import template
# t = template.Template('My name is {{name}}.') # step1
# c = template.Context({'name':'cq_bomb'})      # step2
# t.render(c)                                   # step3
# 'My name is cq_bomb.'

from django.http import HttpResponse
from django import template

def simpleTemplate(request):
    t = template.Template('My name is {{name}}.')
    c = template.Context({'name':'cq_bomb'})
    return HttpResponse(t.render(c))

# 同一个模板,多个上下文(Context)
# t = template.Template('Hello {{name}}!')
# for name in ('tina', 'heymo', 'collinsctk'):
#     print(t.render(template.Context({'name': name})))

def multiContext(request):
    html = "<ul>"
    t = template.Template('<li>Today is {{ day }}.</li>')
    for day in ('Monday', 'Tuesday', 'Wednessday'):
        c = t.render(template.Context({'day':day}))
        html += c
    html += '</ul>'
    return HttpResponse(html)

# 向上下文传递字典和列表
# from django import template
# person = {'name':'tina', 'age':40}
# t = template.Template('{{person.name}} is {{person.age}} years old!')
# c = template.Context({'person':person})
# t.render(c)
# 'tina is 40 years old!'

# person1 = ['tina',40]
# t = template.Template('{{person.0}} is {{person.1}} years old!')
# c = template.Context({'person':person1})
# t.render(c)
# 'tina is 40 years old!'

# 向上下文传递对象(多级深度嵌套)

# t = template.Template('Hello, {{person.name}}')
# c = template.Context({'person':Person()})
# t.render(c)
# 'Hello, tina'
# 查找顺序
# {{person.name}}
# 1. person['name']
# 2. person.name
# 3. person.name()
# 4. person[name]

# 如何处理无效变量
# 变量在模板中存在,但并没有通过Context指定
# 变量区分大小写
# t = template.Template('Hello, {{name}}')
# t.render(template.Context())
# 'Hello, '
# t.render(template.Context({'var':'hello'}))
# 'Hello, '
# t.render(template.Context({'name':'collinsctk'}))
# 'Hello, collinsctk'
# t.render(template.Context({'Name':'collinsctk'}))
# 'Hello, '


# 按照字典方式向Context添加或删除变量
# t = template.Template('This is a {{field1}}. That is a {{field2}}')
# c = template.Context({'field1':'Banana', 'field2':'car'})
# t.render(c)
# 'This is a Banana. That is a car'
# c['field1']
# 'Banana'
# c['field2']
# 'car'
# del c['field1']
# c['field1']
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "/djg_learning/djg_learning/lib/python3.6/site-packages/django/template/context.py", line 83, in __getitem__
#     raise KeyError(key)
# KeyError: 'field1'
# c.get('field1')
# t.render(c)
# 'This is a . That is a car'
# c['field1'] = 'abcd'
# t.render(c)
# 'This is a abcd. That is a car'

# 从磁盘装载模板文件
from django.template.loader import get_template
import datetime


def loadTemplateFile(request):
    now = datetime.datetime.now()
    t = get_template('temp1.html')
    html = t.render({'current_date':now})
    return HttpResponse(html)


from django.shortcuts import render


def loadTemplateFile1(request):
    now = datetime.datetime.now()
    return render(request, 'temp1.html', {'current_date':now})

def loadTemplateFile2(request):
    now = datetime.datetime.now()
    field1 = 'hello'
    field2 = 'world'
    field3 = 'qytang'
    #return render(request, 'temp2.html', {'current_date':now, 'field1':field1, 'field2':field2, 'field3':field3})
    return render(request, 'temp2.html', locals())

# 修改模板目录
# settings.py
# 'DIRS': [os.path.join(BASE_DIR, 'templates')] ,继续添加目录

if __name__ == "__main__":
    pass