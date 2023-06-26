from django.urls import path
from . import views


urlpatterns = [
path('<int:art_id>/', views.detail, name='detail'),
]