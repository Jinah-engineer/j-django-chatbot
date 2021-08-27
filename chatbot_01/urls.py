from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

import chatbot_01.views
from . import views

urlpatterns = [
    path('', chatbot_01.views.home, name="home"),
    path('chattrain', views.chattrain, name='chattrain'),
    path('chatanswer', views.chatanswer, name='chatanswer'),

]