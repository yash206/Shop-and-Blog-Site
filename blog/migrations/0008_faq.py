# Generated by Django 3.1.5 on 2022-05-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20220502_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('FAQ_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=2000)),
            ],
        ),
    ]
