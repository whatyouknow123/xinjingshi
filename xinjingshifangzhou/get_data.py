from models import *


def get_hero_content_warp(num=5):
    if hero_content_wrap.objects.exists():
        return hero_content_wrap.objects.all()[:num]
    return []


def get_hero_icon_boxes(num=3):
    if hero_icon_boxes.objects.exists():
        return hero_icon_boxes.objects.all()[:num]
    return []


def get_home_page_welcome(num=1):
    if home_page_welcome.objects.exists():
        return home_page_welcome.objects.all()[:num]
    return []

def get_home_page_breaking_news(num=1):
    if home_page_breaking_news.objects.exists():
        return home_page_breaking_news.objects.all().order_by('-news_time')[:num]

    return []


def get_base_info(num=1):
    if BaseInfo.objects.exists():
        return BaseInfo.objects.all()[:num]
    return []


def get_breaking_news(num=1):
    if home_page_breaking_news.objects.exists():
        return home_page_breaking_news.objects.order_by('-news_time')[:num]
    return []


def get_all_news(num=20):
    if all_news.objects.exists():
        return all_news.objects.all().order_by('-news_time')[:num]
    return []

def get_bottom_news(num=3):
    if all_news.objects.exists():
        return all_news.objects.all().order_by('-news_time')[:num]
    return []


def get_about_content(num=1):
    if AboutUs.objects.exists():
        return AboutUs.objects.all().order_by('-content_time')[:num]
    return []


def get_leader_words(num=2):
    if LeaderWords.objects.exists():
        return LeaderWords.objects.all().order_by('-time')[:num]
    return []


def get_company_content(num=3):
    if CompanyContent.objects.exists():
        return CompanyContent.objects.all().order_by('-time')[:num]
    return []


def get_company_parter(num=10):
    if CompanyParter.objects.exists():
        return CompanyParter.objects.all().order_by('-time')[:num]
    return []


def get_company_project(num=3):
    if CompanyProject.objects.exists():
        return CompanyProject.objects.all().order_by('-time')[:num]
    return []


def get_looking_parter(num=10):
    if LookingParter.objects.exists():
        return LookingParter.objects.all().order_by('-time')[:num]
    return []


def get_target_and_requirement():
    if TargetAndRequirement.objects.exists():
        return TargetAndRequirement.objects.all()
    return []


def get_common_value():
    base_info = get_base_info()
    bottom_new = get_bottom_news()
    logo = base_info[0].logo_image
    result = {"base_info": base_info, "bottom_new": bottom_new, "logo": logo}
    return result
