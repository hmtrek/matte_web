
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pluss.html', views.pluss, name='pluss'),
    path('minus.html', views.minus, name='minus'),
    path('gange.html', views.gange, name='gange'),
    path('dele.html', views.dele, name='dele'),
]
