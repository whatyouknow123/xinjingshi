# encoding=utf8
from django import forms
from django.core import validators
from models import ApplicationForm, LeaveNote


class TestApplicationForm(forms.Form):
    school = forms.CharField()
    name = forms.CharField(max_length=100,min_length=3,error_messages={'required':'用户名不能为空','min_length':'最少不能少于3个字符','max_length':'最多不能超过100个字符'})
    email = forms.EmailField(error_messages={'invalid':'请输入正确的邮箱!','required':'邮箱不能为空'})
    phone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}',message='请输入正确的手机号码')])
    address = forms.CharField(error_messages={'invalid':'请输入正确的地址!','required':'地址不能为空'})
    age = forms.IntegerField(error_messages={'invalid':'请输入正确的年龄!','required':'年龄不能为空'})
    height = forms.FloatField(error_messages={'invalid':'请输入正确的身高!','required':'身高不能为空'})


def UpdateApplication(result):
    ApplicationForm.objects.create(phone=result["phone"],
                                        school=result['school'],
                                        email=result['email'],
                                        name=result['name'],
                                        address=result['address'],
                                        age=result['age'],
                                        height=result['height'])



class TestLeaveNote(forms.Form):
    name = forms.CharField(max_length=100,min_length=3,error_messages={'required':'用户名不能为空','min_length':'最少不能少于3个字符','max_length':'最多不能超过100个字符'})
    phone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}', message='请输入正确的手机号码')])
    words = forms.CharField(max_length=10000)



def UpdateLeaveNote(result):
    LeaveNote.objects.create(name=result['name'],
                             phone=result['phone'],
                             words=result['words'])