# Generated by Django 2.0 on 2020-01-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200122_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='categories',
            field=models.ManyToManyField(to='myapp.Category'),
        ),
    ]
