# Generated by Django 5.0.1 on 2024-02-04 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0004_author_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Author'),
        ),
    ]
