from django.urls import path
from personal_blog.views.author_views import author_create_view,  AuthorView, AuthorListView

urlpatterns = [
    path('create/', AuthorView.as_view(), name = 'author_create'),
    path('list/', AuthorListView.as_view(), name = 'author_list'),
]