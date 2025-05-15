from django.urls import path
from blog.views import (index, about,
                        add_post, read_post,
                        update_post, delete_post,
                        user_posts, user_info,
                        search_post, filter_post)



app_name = 'blog'
urlpatterns = [
    path('search/', search_post, name='search_post'),
    path('filter/', filter_post, name='filter_post'),
    path('about/', about, name='about'),
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
    path('post/user/info/<int:user_id>/', user_info, name='user_info'),
    path('post/user/<int:user_id>/', user_posts, name='user_posts'),
    path('post/<int:pk>/edit/', update_post, name='update_post'),
    path('post/<slug:slug>/', read_post, name='read_post'),
    path('post/', add_post, name='add_post'),
    path('', index, name='index'),
]