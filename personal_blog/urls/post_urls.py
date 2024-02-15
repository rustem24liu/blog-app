from django.urls import path
from personal_blog.views.post_views_classView import PostDetailView, CommentView, PostCreateView, PostUpdateView, PostListView
from personal_blog.views.post_views_functions import post_create_view, post_list_view, post_update_view, post_delete_view, post_detail_view

urlpatterns = [
    path('detail/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('create/', PostCreateView.as_view(), name="post_create"),
    path('list/', PostListView.as_view(), name='post_list'),
    path('update/<int:pk>', post_update_view, name="post_update"),
    path('delete/<int:pk>', post_delete_view, name="post_delete"),
    path('detail/<int:post_pk>/comment/create', CommentView.as_view(), name="comment_create"),
]