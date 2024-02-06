from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Name of the author')

    def __str__(self):  # method str like in java
        return f"{self.pk}. {self.name}"


class Post(models.Model):
    title = models.CharField (max_length=200, null=False, blank=False, verbose_name="Header")

    body = models.TextField (max_length = 3000, null=False, blank=False, verbose_name="Body of the post")

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Author", null=False, blank=False)
    # author = models.CharField(max_length=100, null=False, blank=False, verbose_name='Author')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Data")

    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Data")

    # class может иметь множество методов но сейчась расмотрим только важных

    def __str__(self):  # method str like in java
        return f"{self.pk} - {self.title} by {self.author}"

    class Meta:
        pass

class Comment(models.Model):
    text = models.TextField (max_length=1000, null=False, blank=False, verbose_name='Comment')
    author = models.CharField(max_length=50, null=False, blank=False, default="Anonymous", verbose_name="Author")

    post = models.ForeignKey('personal_blog.Post', on_delete=models.CASCADE, related_name='Comments', verbose_name="Post")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Data")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Data")

    def __str__(self) :
        return f"{self.text[:20]} by {self.author}"

