from django.shortcuts import render
from .models import AboutPicture

# Create your views here.

def about(request):
    pic = AboutPicture.objects
    return render(request, 'about.html', {'pic':pic})