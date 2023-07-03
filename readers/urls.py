from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login_reader/', views.login_reader, name='login_reader'),
    path('logout_reader/', views.logout_reader, name='logout_reader'),
    path('profile', views.profile, name='profile'),
]