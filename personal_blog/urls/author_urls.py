from django.urls import path
from personal_blog.views.author_views import author_create_view, author_list_view

urlpatterns = [
    path('create/', author_create_view, name = 'author_create'),
    path('list/', author_list_view, name = 'author_list'),
]