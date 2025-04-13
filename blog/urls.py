from django.urls import path
from blog.views import index, about, add_post, read_post, update_post



app_name = 'blog'
urlpatterns = [
    path('about/', about, name='about'),
    path('post/<int:pk>/edit/', update_post, name='update_post'),
    path('post/<int:pk>/', read_post, name='read_post'),
    path('post/', add_post, name='add_post'),
    path('', index, name='index'),
]