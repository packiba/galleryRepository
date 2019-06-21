from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Picture


class PictureListView(ListView):
    model = Picture
    template_name = 'gallery/list.html'

class PictureDetailView(DetailView):
    model = Picture
    template_name = 'gallery/detail.html'