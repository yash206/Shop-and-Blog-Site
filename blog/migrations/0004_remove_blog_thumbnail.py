# Generated by Django 3.1.5 on 2022-05-02 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='thumbnail',
        ),
    ]
