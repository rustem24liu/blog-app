from django.urls import path
from personal_blog.views.post_views import PostDetailView, post_create_view, post_list_view, post_update_view, post_delete_view, CommentView


urlpatterns = [
    path('detail/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('create/', post_create_view, name="post_create"),
    path('list/', post_list_view, name='post_list'),
    path('update/<int:pk>', post_update_view, name="post_update"),
    path('delete/<int:pk>', post_delete_view, name="post_delete"),
    path('detail/<int:post_pk>/comment/create', CommentView.as_view(), name="comment_create"),
]