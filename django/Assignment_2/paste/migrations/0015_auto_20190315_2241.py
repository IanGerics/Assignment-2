# Generated by Django 2.1.7 on 2019-03-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0014_merge_20190315_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='permissioned_users',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
