from django.urls import path
from blog.views import index, about


app_name = 'blog'
urlpatterns = [
    path('about/', about, name='about'),
    path('', index, name='index'),
]