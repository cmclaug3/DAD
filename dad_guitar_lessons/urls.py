"""dad_guitar_lessons URL Configuration

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

from schedule.views import home, lesson_main, lesson_submit, login_view, logout_view
from todos.views import todos, new_todo

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^lessons/', lesson_main, name='lesson_main'),
    url(r'^$', login_view, name='login_view'),
    url(r'^logout/', logout_view, name='logout_view'),
    url(r'^todos/', todos, name='todos'),
    url(r'^new_todo/', new_todo, name='new_todo'),
    url(r'^home/', home, name='home'),
    

]
