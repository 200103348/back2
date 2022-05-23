# Generated by Django 4.0.4 on 2022-05-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=400)),
                ('title', models.CharField(max_length=200)),
                ('info', models.TextField(max_length=1000)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
    ]