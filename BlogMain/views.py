from django.shortcuts import render

# Create your views here.
def BlogMainHtml(request):
    return render(request, 'main/blog_main.html')
