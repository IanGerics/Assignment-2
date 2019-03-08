from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='paste-home'),
	path('about/', views.about, name='paste-about'),
]