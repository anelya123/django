from django.contrib import admin
from django.urls import path, include
from btest import views

urlpatterns = [
	path('', views.index),
	path('', views.about),
	path ('admin/', admin.site.urls)
]
