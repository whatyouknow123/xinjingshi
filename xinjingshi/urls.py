"""xinjingshi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from xinjingshifangzhou import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name="index"),
    url(r'^about/$', views.about, name='about'),
    url(r'^causes/', views.causes, name='causes'),
    url(r'^concat/', views.contact, name="concat"),
    url(r'^elements/', views.elements, name='elements'),
    url(r'^portfolio', views.portfolio, name='portfolio'),
    url(r'^single-causes/', views.single_causes, name='single-causes'),
    url(r'^single-news/', views.single_news, name='single-news'),
    url(r'^admin/', admin.site.urls)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)