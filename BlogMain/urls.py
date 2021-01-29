from django.urls import path, re_path
from BlogMain.views import *
from BlogMain import views

app_name = 'BlogMain'
urlpatterns = [
    path('',views.TopLV.as_view(),name='top_listview'),
]
