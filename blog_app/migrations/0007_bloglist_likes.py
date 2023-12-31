# Generated by Django 4.2 on 2023-07-12 09:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0006_remove_bloglist_blog_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloglist',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='like_blog', to=settings.AUTH_USER_MODEL),
        ),
    ]
