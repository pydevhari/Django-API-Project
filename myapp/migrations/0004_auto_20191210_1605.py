# Generated by Django 2.2.7 on 2019-12-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20191210_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='result',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='marks',
            name='total',
            field=models.IntegerField(default=10),
        ),
    ]
