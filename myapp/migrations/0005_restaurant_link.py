# Generated by Django 2.0 on 2020-01-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200119_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='link',
            field=models.URLField(default='https://www.tripadvisor.es'),
        ),
    ]
