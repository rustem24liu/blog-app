from django.contrib import admin
from django.urls import path
from personal_blog.views import post_detail_view, post_create_view, post_list_view, post_update_view, post_delete_view


urlpatterns = [
    path('detail/<int:pk>', post_detail_view, name="post_detail"),
    path('create/', post_create_view, name="post_create"),
    path('list/', post_list_view, name='post_list'),
    path('update/<int:pk>', post_update_view, name="post_update"),
    path('delete/<int:pk>', post_delete_view, name = "post_delete")
]