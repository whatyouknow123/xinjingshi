# encoding=utf8
from django.shortcuts import render
from get_data import *
from .forms import *
from .models import ApplicationForm
from django.shortcuts import HttpResponse
from django.contrib import messages
import json

def index(request):
    wrapper = get_hero_content_warp()
    boxes = get_hero_icon_boxes()
    welcome = get_home_page_welcome()
    breaking_news = get_home_page_breaking_news()
    breaking_news_title = ""
    breaking_news_content = ""
    if len(breaking_news) > 0:
        breaking_news_title = breaking_news[0].news_title
        breaking_news_content = breaking_news[0].news_content
    result = {"wrapper": wrapper, "boxes": boxes, "welcome": welcome,
              "breaking_news_title": breaking_news_title, "breaking_news_content": breaking_news_content}
    common_value = get_common_value()
    for key, value in common_value.items():
        result[key] = value
    return render(request, 'index.html', result)


def about(request):
    about_us_value = get_about_content()
    leader_words_value = get_leader_words()
    result = {"about_content": about_us_value,
              "leader_words": leader_words_value}
    common_value = get_common_value()
    for key, value in common_value.items():
        result[key] = value
    return render(request, 'about.html', result)


def base(request):
    base_info, bottom_new, logo = get_common_value()
    return render(request, 'bottom.html', {"base_info": base_info})


def causes(request):
    company_content = get_company_content()
    company_parter = get_company_parter()
    company_project = get_company_project()
    result = {
        "company_content": company_content,
        "company_parter": company_parter,
        "company_project": company_project
    }
    common_value = get_common_value()
    for key, value in common_value.items():
        result[key] = value
    descrption = result['base_info'][0].company_description
    result["company_description"] = descrption
    company_image = result['base_info'][0].company_image
    result["company_image"] = company_image
    return render(request, 'causes.html', result)


def contact(request):
    result = {}
    common_value = get_common_value()
    for key, value in common_value.items():
        result[key] = value
    company_des = result['base_info'][0].company_description
    company_phone = result['base_info'][0].phone
    company_mail = result['base_info'][0].mail
    company_address = result['base_info'][0].location
    result['company_phone'] = company_phone
    result['company_mail'] = company_mail
    result['company_address'] = company_address
    result['company_description'] = company_des
    submit_string = "留言失败"
    if request.method == "POST":
        form = TestLeaveNote(request.POST)
        # exist = TargetAndRequirement.objects.filter(phone=form.cleaned_data.get('phone')).exists()
        if form.is_valid():
            #print form.is_valid()
            tmp_result = {"name": form.cleaned_data.get('name'),
                          "phone": form.cleaned_data.get('phone'),
                          "words": form.cleaned_data.get('words')}
            for each in tmp_result:
                print(each, tmp_result[each])
            UpdateLeaveNote(tmp_result)
            submit_string = "成功留言"


        else:

            submit_string = "您填入了无效信息"

            # if not exist:
            #    return HttpResponse("the phone already exist")
        result["submit_string"] = submit_string

        messages.add_message(request, messages.INFO, submit_string)

    return render(request, 'contact.html', result)


def elements(request):
    return render(request, 'elements.html')


def portfolio(request):
    lookingparter = get_looking_parter()
    result = {"lookingparter": lookingparter}
    common_value = get_common_value()
    for key, value in common_value.items():
        result[key] = value
    result["winwin_descriotion"] = result['base_info'][0].winwin_description
    result["winwin_image"] = result["base_info"][0].winwin_image
    return render(request, 'portfolio.html', result)


def single_causes(request):
    result = {"target": get_target_and_requirement()}
    common_value = get_common_value()
    for key, value in common_value.items():
        result[key] = value

    descrption = result['base_info'][0].company_description
    result["company_description"] = descrption
    company_image = result['base_info'][0].company_image
    result["company_image"] = company_image
    submit_string = "成功报名"
    if request.method == "POST":
        form = TestApplicationForm(request.POST)
        #exist = TargetAndRequirement.objects.filter(phone=form.cleaned_data.get('phone')).exists()
        if form.is_valid():
            phone_num = form.cleaned_data.get('phone')
            exist = ApplicationForm.objects.filter(phone=phone_num).exists()
            if exist:
                submit_string = "您的电话已被注册"
            else:

                tmp_result = {"name": form.cleaned_data.get('name'),
                      "type": form.cleaned_data.get('type'),
                      "phone": form.cleaned_data.get('phone'),
                      "age": form.cleaned_data.get('age'),
                      "gender": form.cleaned_data.get('gender')}
                UpdateApplication(tmp_result)


        else:

            submit_string = "您填入了无效信息"
        messages.add_message(request, messages.INFO, submit_string)
        result["message"] = submit_string

    return render(request, 'single-causes.html', result)



def single_news(request):
    all_news = get_all_news()
    base_info = get_base_info()
    bottom_news = get_bottom_news()
    result = {"all_news": all_news, "base_info": base_info, "bottom_new": bottom_news}
    return render(request, 'single-news.html', result)




