"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from newmovie.views import newmovie
from onmovie.views import onmovie
from comingmovie.views import comingmovie
from rank.views import rank
from new.views import new
from onmovie.views import index
from message.views import message
from address.views import address


urlpatterns = [
    path('admin/', admin.site.urls),
    path('newmovie/', newmovie),
    path('onmovie/', onmovie),
    path('comingmovie/', comingmovie),
    path('rank/', rank),
    path('new/', new),
    path('',index),
    path('message/', message),
    path('address/', address),

]
