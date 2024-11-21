# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from .views import send_email

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('send_email/', send_email, name='send_email'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
