# Generated by Django 2.1.2 on 2018-10-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, upload_to='author_image'),
        ),
    ]
