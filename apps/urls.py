from django.urls import path
from .views import (
    LoginView,
    IndexView, RegisterView, ServiceView, ContactView
)

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('login',LoginView.as_view(), name='login'),
    path('register/',RegisterView.as_view(), name='register'),
    path('service', ServiceView.as_view(), name='service'),
    path('contact', ContactView.as_view(), name='contact'),
]


