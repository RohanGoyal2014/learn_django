from django.urls import re_path
from . import views

app_name='auth_app'

urlpatterns = [
    re_path('register/',views.register_page,name='register'),
    re_path('login/',views.login_page,name='login'),
    re_path('logout/',views.user_logout,name='logout'),
    re_path('special/',views.special,name='special'),
    re_path('', views.index,name='index'),
]