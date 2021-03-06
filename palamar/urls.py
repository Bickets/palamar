"""palamar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admindj/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^auth/', include('authcp.urls')),
    url(r'^admincp/sites/', include('sites.urls')),
    url(r'^container/', include('container.urls')),
    url(r'^domain/', include('domain.urls')),
    url(r'^image/', include('image.urls')),
    url(r'^network/', include('network.urls')),
    url(r'^project/', include('project.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^volume/', include('volume.urls')),
]
