from django.urls import path,re_path,include
from . import views

urlpatterns = [
    re_path('form/',views.form,name='form'),
re_path('', views.index,name='index'),
]