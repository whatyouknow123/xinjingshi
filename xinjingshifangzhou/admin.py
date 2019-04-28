# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(hero_content_wrap)
admin.site.register(hero_icon_boxes)
admin.site.register(home_page_welcome)
admin.site.register(home_page_breaking_news)
admin.site.register(BaseInfo)
admin.site.register(all_news)
admin.site.register(AboutUs)
admin.site.register(LeaderWords)
admin.site.register(CompanyContent)
admin.site.register(CompanyParter)
admin.site.register(CompanyProject)
admin.site.register(LookingParter)
admin.site.register(TargetAndRequirement)
admin.site.register(ApplicationForm)
admin.site.register(LeaveNote)