# Generated by Django 3.0.8 on 2020-07-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20200712_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.CharField(default='', max_length=300),
        ),
    ]
