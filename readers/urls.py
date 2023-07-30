from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_reader, name='register'),
    path('login/', views.login_reader, name='login'),
    path('logout/', views.logout_reader, name='logout'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('account/', views.account, name='account'),
    path('edit_account/', views.edit_account, name='edit_account'),
]