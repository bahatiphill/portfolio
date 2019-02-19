# Generated by Django 2.1.5 on 2019-02-19 13:44

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('tags', models.CharField(max_length=40)),
                ('slug', models.SlugField(unique=True)),
                ('publish', models.BooleanField(default=False)),
                ('title_image', models.ImageField(upload_to='title_images/')),
            ],
        ),
    ]
