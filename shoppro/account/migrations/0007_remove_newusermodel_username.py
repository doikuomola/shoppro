# Generated by Django 3.2 on 2021-04-28 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_newusermodel_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newusermodel',
            name='username',
        ),
    ]
