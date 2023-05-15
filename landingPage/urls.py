from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name = 'landingPage'),
    path('', views.get, name = 'landingPageGet'),
    path('', views.post, name = 'landingPagePost'),
]