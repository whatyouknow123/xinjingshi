
from django.db import models
from django.contrib import admin


class BaseInfo(models.Model):
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    consult_image = models.FileField(upload_to='base_info')
    scan_image = models.FileField(upload_to='base_info')
    logo_image = models.FileField(upload_to='base_info')
    company_description = models.TextField()
    company_image = models.FileField(upload_to="base_info")
    winwin_description = models.TextField()
    winwin_image = models.FileField(upload_to='base_info')
    def __unicode__(self):
        return self.phone


class hero_content_wrap(models.Model):
    entry_header_name = models.CharField(max_length=100)
    entry_header_title = models.CharField(max_length=200)
    entry_header_content = models.TextField()
    entry_image = models.FileField(upload_to='hero_content_wrap')

    def __unicode__(self):
        return self.entry_image.url


class hero_icon_boxes(models.Model):
    entry_title = models.CharField(max_length=100)
    entry_content = models.TextField()
    image_name_white = models.FileField(upload_to='hero_icon_boxes')
    image_name_grey = models.FileField(upload_to='hero_icon_boxes')

    def __unicode__(self):
        return self.entry_title


class home_page_welcome(models.Model):
    entry_header = models.CharField(max_length=100)
    entry_content = models.TextField()
    image_welcome = models.FileField(upload_to='home_page_welcome')

    def __unicode__(self):
        return self.entry_header


class home_page_breaking_news(models.Model):
    news_title = models.CharField(max_length=50)
    news_content = models.TextField()
    news_time = models.DateTimeField()

    def __unicode__(self):
        return self.news_title


class all_news(models.Model):
    news_title = models.CharField(max_length=50)
    news_content = models.TextField()
    news_time = models.DateTimeField()
    news_image = models.FileField(upload_to="all_news")

    def __unicode__(self):
        return self.news_title


class AboutUs(models.Model):
    about_content = models.TextField()
    about_image = models.FileField(upload_to="about_us")
    content_time = models.DateTimeField()

    def __unicode__(self):
        return self.about_content[:20]


class LeaderWords(models.Model):
    leader_name = models.CharField(max_length=20)
    leader_type = models.CharField(max_length=100)
    leader_words = models.TextField()
    leader_image = models.FileField(upload_to="leader_words")

    time = models.DateTimeField()


    def __unicode__(self):
        return self.leader_name


class CompanyContent(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    time = models.DateTimeField()
    current_image = models.FileField()

    def __unicode__(self):
        return self.name


class CompanyProject(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    time = models.DateTimeField()
    current_image = models.FileField()

    def __unicode__(self):
        return self.name


class CompanyParter(models.Model):
    name = models.CharField(max_length=50)
    time = models.DateTimeField()
    current_image = models.FileField()

    def __unicode__(self):
        return self.name


class LookingParter(models.Model):
    name = models.CharField(max_length=50)
    time = models.DateTimeField()
    current_image = models.FileField()
    content = models.TextField()

    def __unicode__(self):
        return self.name


class TargetAndRequirement(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()

    def __unicode__(self):
        return self.name


class ApplicationForm(models.Model):
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    #email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    #address = models.CharField(max_length=200)
    age = models.BigIntegerField()
    #height = models.FloatField()
    gender = models.CharField(max_length=50)

    def __unicode__(self):
        return self.phone


class LeaveNote(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    words = models.TextField()

    def __unicode__(self):
        return self.name







