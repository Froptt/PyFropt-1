# Generated by Django 2.2 on 2021-11-29 23:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_delete_iletisim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=1000, verbose_name='İçerik (255) Karakter'),
        ),
    ]