from django.shortcuts import render
from django.views.generic import ListView,View
from board.models import Post

# Create your views here.
class TopLV(ListView):
    model = Post
    template_name = 'main/blog_main.html'
    context_object_name = 'posts'
