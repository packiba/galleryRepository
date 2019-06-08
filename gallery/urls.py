from django.urls import path
from . import views

urlpatterns = [
    path('', views.Mylist.as_view(), name='pictures'),
    # path('', views.mylist, name='pictures'),
]