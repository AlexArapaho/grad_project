from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    # path('contact/', views.contact_send_mail, name='contact'),
]