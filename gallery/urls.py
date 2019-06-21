from django.urls import path
from . import views

urlpatterns = [
    path('', views.PictureListView.as_view(), name='home'),
    path('<int:pk>', views.PictureDetailView.as_view(), name='detail'),
]
