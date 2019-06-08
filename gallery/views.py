from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.utils import timezone
from .models import Picture


# def mylist(request):
# #     pictures = Picture.objects.all()
# #     return render(request, 'gallery/list.html')

class Mylist(ListView):
    model = Picture
    template_name = 'gallery/list.html'