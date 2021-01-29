from django.urls import path,re_path
from board import views

app_name = 'board'
urlpatterns = [
    # Ex /board/
    path('',views.PostLV.as_view(),name='index'),

    # Ex /board/post/
    path('post/',views.PostLV.as_view(),name='post_list'),

    # Ex /board/post/django-example/
    re_path(r'^post/(?P<slug>[-\w\d ]+)/$',views.PostDV.as_view(),name='post_detail'),

    # Ex /board/archive/
    path('archive/',views.PostAV.as_view(),name='post_archive'),

    # Ex /board/archive/2021/
    path('archive/<int:year>/',views.PostYAV.as_view(),name='post_year_archive'),

    # Ex /board/archive/2021/jan/
    path('archive/<int:year>/<str:month>/',views.PostMAV.as_view(),name='post_month_archive'),

    # Ex /board/archive/2021/jan/10/
    path('archive/<int:year>/<str:month>/<int:day>/',views.PostDAV.as_view(),name='post_day_archive'),

    # Ex /board/archive/today/
    path('archive/today/',views.PostTAV.as_view(),name='post_today_archive'),

    # Ex /blog/tag/
    path('tag/',views.TagCloudTV.as_view(),name='tag_cloud'),

    # Ex /blog/tag/tagname/
    path('tag/<str:tag>/',views.TaggedObjectLV.as_view(),name='tagged_object_list'),

    path('CreatePost/',views.CreatePost,name='CreatePost'),
]
