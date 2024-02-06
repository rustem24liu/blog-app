# Generated by Django 5.0.1 on 2024-02-05 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0006_alter_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Comment')),
                ('author', models.CharField(blank=True, default='Anonymous', max_length=50, null=True, verbose_name='Author')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Data')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Data')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='personal_blog.post', verbose_name='Post')),
            ],
        ),
    ]