# Generated by Django 5.0.1 on 2024-01-31 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='content',
        ),
    ]
