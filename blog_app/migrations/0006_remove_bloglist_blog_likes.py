# Generated by Django 4.2 on 2023-06-30 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_bloglist_blog_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloglist',
            name='Blog_likes',
        ),
    ]