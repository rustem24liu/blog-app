from django.contrib import admin
from personal_blog.models import Post
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    list_filter = ['author']
    search_fields = ['title', 'body']
    fields = ['title', 'body', 'author', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']



admin.site.register(Post, PostAdmin)