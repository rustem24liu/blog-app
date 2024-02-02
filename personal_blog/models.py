from django.db import models

class Post(models.Model):
    title = models.CharField (max_length=200, null=False, blank=False, verbose_name="Header")

    body = models.TextField (max_length = 3000, null=False, blank=False, verbose_name="Body of the post")

    author = models.CharField(max_length=100, null = False, blank=False, verbose_name="I am the author of this book")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Data")

    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Data")

    # class может иметь множество методов но сейчась расмотрим только важных

    def __str__(self):  # method str like in java
        return f"{self.pk} - {self.title} by {self.author}"

    class Meta:
        pass