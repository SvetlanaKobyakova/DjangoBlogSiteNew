from django.urls import path
from .views import register, log_in, log_out, user_profile


app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('profile/<int:pk>/', user_profile, name='profile'),
]