# Generated by Django 2.1.7 on 2019-03-15 17:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0010_post_shares'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='shares',
            field=models.ManyToManyField(blank=True, related_name='shares', to=settings.AUTH_USER_MODEL),
        ),
    ]
