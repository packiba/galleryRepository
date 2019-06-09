# from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Picture


# class Mylist(ListView):
#     template_name = 'gallery/list.html'

def piclist(request):
    images = Picture.objects.all()
    return render(request, 'gallery/list.html', {'images': images})
