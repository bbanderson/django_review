from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def home(request):
    blogQuerySet = Blog.objects
    return render(request, 'home.html', {'blogs':blogQuerySet})

def detail(request, conti_id):
    conti_detail = get_object_or_404(Blog, pk = conti_id)
    return render(request, 'detail.html', {'detail':conti_detail})