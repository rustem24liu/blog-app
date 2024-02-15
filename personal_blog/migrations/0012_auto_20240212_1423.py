# Generated by Django 5.0.1 on 2024-02-12 14:23

from django.db import migrations

def transfer_tags(apps, schema_editor):
    Post = apps.get_model("personal_blog.Post")
    for post in Post.objects.all():
        post.tags.set(post.tags_old.all())

def rollback_transfer(apps, schema_editor):
    Post = apps.get_model("personal_blog.Post")
    for post in Post.objects.all():
        post.tags_old.set(post.rags)(-1)
class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0011_post_tags_alter_post_tags_old'),
    ]

    operations = [
        migrations.RunPython(transfer_tags, rollback_transfer)
    ]