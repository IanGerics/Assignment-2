# Generated by Django 2.1.7 on 2019-03-13 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0005_auto_20190313_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]
