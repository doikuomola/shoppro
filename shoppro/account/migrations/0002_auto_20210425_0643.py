# Generated by Django 3.2 on 2021-04-25 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password1',
            field=models.CharField(default='password', max_length=40),
        ),
        migrations.AddField(
            model_name='register',
            name='password2',
            field=models.CharField(default='password', max_length=40),
        ),
    ]