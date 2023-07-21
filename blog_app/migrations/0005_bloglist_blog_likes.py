# Generated by Django 4.2 on 2023-06-30 07:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0004_alter_bloglist_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloglist',
            name='Blog_likes',
            field=models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
