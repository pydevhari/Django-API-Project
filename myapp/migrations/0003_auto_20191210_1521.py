# Generated by Django 2.2.7 on 2019-12-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191128_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField()),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=10)),
                ('obt', models.IntegerField()),
                ('remark', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='HariSh',
        ),
    ]
