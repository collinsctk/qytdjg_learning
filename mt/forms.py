#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=10, min_length=5, label='姓名') #限制最小和最大值
    email = forms.EmailField(required=False, widget=forms.DateInput, label='Email地址')
    message = forms.CharField(widget=forms.Textarea, label='信息') #文本框类型
    def clean_message(self): # 名字需要注意 是组合
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('单词数不能小于4')
        return message

# from mt.forms import MyForm

# my = MyForm()
# print(my)
# <tr><th><label for="id_name">Name:</label></th><td><input type="text" name="name" required id="id_name" /></td></tr>
# <tr><th><label for="id_email">Email:</label></th><td><input type="email" name="email" id="id_email" /></td></tr>
# <tr><th><label for="id_message">Message:</label></th><td><input type="text" name="message" required id="id_message" /></td></tr>

# print(my.as_ul())
# <li><label for="id_name">Name:</label> <input type="text" name="name" required id="id_name" /></li>
# <li><label for="id_email">Email:</label> <input type="email" name="email" id="id_email" /></li>
# <li><label for="id_message">Message:</label> <input type="text" name="message" required id="id_message" /></li>

# print(my.as_p())
# <p><label for="id_name">Name:</label> <input type="text" name="name" required id="id_name" /></p>
# <p><label for="id_email">Email:</label> <input type="email" name="email" id="id_email" /></p>
# <p><label for="id_message">Message:</label> <input type="text" name="message" required id="id_message" /></p>

# print(my['name'])
# <input type="text" name="name" required id="id_name" />
# print(my['message'])
# <input type="text" name="message" required id="id_message" />

# my1 = MyForm({'name':'Hello','email':'1@2.net','message':'abcd'})
# my1.is_valid()
# True
# my2 = MyForm({'name':'Hello','message':'abcd'})
# my2.is_valid()
# True

# my2 = MyForm({'name':'Hello','email':'net','message':'abcd'})
# my2.is_valid()
# False

# my3 = MyForm({'name':'Hello','email':'net'})
# my3.is_valid()
# False

# my3['name'].errors
# []
# my3['email'].errors
# ['Enter a valid email address.']
# my3['message'].errors
# ['This field is required.']


if __name__ == "__main__":
    pass