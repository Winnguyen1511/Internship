from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
# Create your views here.

# posts = [
#     {
#         'author': 'Winnguyen1511', 
#         'title': 'Blog Post 1', 
#         'content': 'Fisrt post content', 
#         'date_posted':'August 27, 2020'
#     },
#     {
#         'author': 'Hiennguyen', 
#         'title': 'Blog Post 2', 
#         'content': 'Second post content', 
#         'date_posted':'August 28, 2020'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    #Pass data to the render.
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
