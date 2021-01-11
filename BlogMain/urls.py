from django.urls import path, re_path
from BlogMain.views import *

app_name = 'BlogMain'
urlpatterns = [
    path('',BlogMainHtml,name = 'BlogMainHtml'),
]
